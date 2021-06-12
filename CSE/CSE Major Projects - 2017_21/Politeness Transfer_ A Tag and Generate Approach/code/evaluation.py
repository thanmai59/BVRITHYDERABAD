# -*- coding: utf-8 -*-


import json
import spacy
import numpy as np
import pandas as pd
from tqdm import tqdm
from collections import defaultdict

from perception_utils import estimate_perception

from convokit import Corpus, Utterance, Speaker
from convokit import TextParser, PolitenessStrategies

from bleu import get_bleu

mt_corpus = Corpus(filename="data/test/mt-test-corpus")
ind_corpus = Corpus(filename="data/test/ind-test-corpus/")

individuals = ['average', 'A23', 'A2U', 'A1F', 'A3S', 'AYG']

perception_models = defaultdict()

for ind in individuals:
    with open("data/perceptions/{}.json".format(ind), 'r') as f:
        perception_models[ind] = json.load(f)
        
at_risk_strategies = {'Subjunctive', "Please", 'Filler', "Swearing"}

ps = PolitenessStrategies(strategy_attribute_name = "strategies", \
                          marker_attribute_name = "markers", \
                          strategy_collection="politeness_local")

spacy_nlp = spacy.load('en', disable=['ner'])

# get politeness strategies for the test utterances 
mt_corpus = ps.transform(mt_corpus, markers=True)

# get politeness strategies for the back translations 
translated_strategies = {utt.id: ps.transform_utterance(utt.meta['back_translation'], \
                                                        spacy_nlp=spacy_nlp, markers=True) for utt in mt_corpus.iter_utterances()}

ind_corpus = ps.transform(ind_corpus, markers=True)

# for readability, we save the strategy set present as seperate meta data 
for corpus in [mt_corpus, ind_corpus]:
    
    for utt in corpus.iter_utterances():
        
        utt.meta['strategy_set'] = {k for k,v in utt.meta['strategies'].items() if v ==1}
        
# We use the "average person" model as both the sender and the receiver
average_model = perception_models['average']

for utt in mt_corpus.iter_utterances():
    
    strategies_used = utt.meta['strategy_set']
    strategies_preserved = {k for k, v in translated_strategies[utt.id].meta['strategies'].items() if v == 1}
    
    utt.meta['intended_politeness'] = estimate_perception(average_model, strategies_used)
    utt.meta['perceived_politeness'] = estimate_perception(average_model, strategies_preserved)
    
for utt in ind_corpus.iter_utterances():
    
    strategies_used = utt.meta['strategy_set']
    
    sender_model = perception_models[utt.meta['sender']]
    receiver_model = perception_models[utt.meta['receiver']]
    
    utt.meta['intended_politeness'] = estimate_perception(sender_model, strategies_used)
    utt.meta['perceived_politeness'] = estimate_perception(receiver_model, strategies_used)
    
print("MAE: No intervention")

print("\t Translated communication: {:.2f}".format(np.mean([abs(utt.meta['intended_politeness'] - utt.meta['perceived_politeness']) \
                                                            for utt in mt_corpus.iter_utterances()])))
      
print("\t Translated communication: {:.2f}".format(np.mean([abs(utt.meta['intended_politeness'] - utt.meta['perceived_politeness']) \
                                                            for utt in ind_corpus.iter_utterances()])))
    
import imp
import plan_with_ilp

from plan_with_ilp import get_ilp_solution
# For Experiment A, we consider average perception models, and account for the set of at-risk strategies
mt_ilp_solutions = {utt.id: get_ilp_solution(utt.id, utt.meta['strategy_set'], \
                                          average_model, average_model, \
                                          at_risk_strategies) for utt in tqdm(mt_corpus.iter_utterances())}
    
# For Experiment B, we consider individualized perception models, and all strategies are considered safe
ind_ilp_solutions = {utt.id: get_ilp_solution(utt.id, utt.meta['strategy_set'], \
                                          perception_models[utt.meta['sender']], \
                                          perception_models[utt.meta['receiver']], set()) for utt in tqdm(ind_corpus.iter_utterances())}
    
from plan_with_baselines import get_greedy_plan
mt_greedy_solutions = {utt.id: get_greedy_plan(utt.meta['strategy_set'], average_model, average_model, \
                                              at_risk_strategies) for utt in mt_corpus.iter_utterances()}

ind_greedy_solutions = {utt.id: get_greedy_plan(utt.meta['strategy_set'], \
                                                perception_models[utt.meta['sender']], \
                                                perception_models[utt.meta['receiver']], set()) for utt in ind_corpus.iter_utterances()}
    
from plan_with_baselines import init_transformer, add_similarity_scores, get_retrieval_plan
from strategy_manipulation import remove_strategies_from_utt

# We only search from reference utterances that has the same polarity as the input
# Thus we need information on the polarity of the texts 

def add_estimated_polarity(utt, perception_model, polarity_attribute_name):
    
    # 1 = polite, 0 = impolite
    polarity = int(estimate_perception(perception_model, utt.meta['strategy_set']) >= 0)
    
    utt.meta[polarity_attribute_name] = polarity
    
    return polarity

# loading the training (reference) corpus
train_corpus = Corpus(filename="data/train/training-corpus")

# obtain politeness annotations 
train_corpus = ps.transform(train_corpus, markers=True)

for utt in train_corpus.iter_utterances():
    utt.meta['strategy_set'] = {k for k,v in utt.meta['strategies'].items() if v ==1}
    
# preparing corpuses: adding polarity, and getting marker-removed contents

# for the training corpus and experiment A, we use the average person model to judge polarity  
for corpus in [train_corpus, mt_corpus]:
    
    for utt in corpus.iter_utterances():
    
        remove_strategies_from_utt(utt, utt.meta['strategy_set'], \
                                   removed_attribute_name="content")

        add_estimated_polarity(utt, average_model, "polarity")
    
# for experiment B, we judge polarity from the sender's perspective 
for utt in ind_corpus.iter_utterances():

    remove_strategies_from_utt(utt, utt.meta['strategy_set'], \
                               removed_attribute_name="content")
    
    add_estimated_polarity(utt, perception_models[utt.meta['sender']], "polarity")
    
# we compare contents of utterances with their tfidf representation  
tfidf = init_transformer(train_corpus)

# for each utterance in test corpus, we obtain the cosine similarity scores with each utterance in the training corpus
mt_corpus = add_similarity_scores(mt_corpus, train_corpus, tfidf)
ind_corpus = add_similarity_scores(ind_corpus, train_corpus, tfidf)

train_ids = train_corpus.get_vector_matrix('tfidf').ids

mt_retrieval_solutions = {utt.id: get_retrieval_plan(utt, train_corpus, train_ids, \
                                                     at_risk_strategies) for utt in mt_corpus.iter_utterances()}

ind_retrieval_solutions = {utt.id: get_retrieval_plan(utt, train_corpus, train_ids, \
                                                      set()) for utt in ind_corpus.iter_utterances()}
    
def add_plan_to_corpus(corpus, solutions, solution_attribute_name):
    
    for idx, sol in solutions.items():
        
        corpus.get_utterance(idx).meta[solution_attribute_name] = sol
        
# Experiment A
mt_plans = {'ilp_plan': mt_ilp_solutions, 'greedy_plan': mt_greedy_solutions, 'retrieval_plan': mt_retrieval_solutions}

for attribute_name, plan in mt_plans.items():
    
    add_plan_to_corpus(mt_corpus, plan, attribute_name)
    
# Experiment B
ind_plans = {'ilp_plan': ind_ilp_solutions, 'greedy_plan': ind_greedy_solutions, 'retrieval_plan': ind_retrieval_solutions}

for attribute_name, plan in ind_plans.items():
    
    add_plan_to_corpus(ind_corpus, plan, attribute_name)
    
print("Experiment A")
print("------------")

print("MAE_plan")
for plan in ['retrieval_plan', 'greedy_plan', 'ilp_plan']:
    
    print('\t{}: {:.2f}'.format(plan.upper(), np.mean([abs(estimate_perception(average_model, utt.meta[plan]) - \
             utt.meta['intended_politeness']) for utt in mt_corpus.iter_utterances()])))
    
print("#-ADDED")
for plan in ['retrieval_plan', 'greedy_plan', 'ilp_plan']:
    
    print('\t{}: {:.2f}'.format(plan.upper(), \
                                np.mean([len(utt.meta[plan] - utt.meta['strategy_set']) for utt in mt_corpus.iter_utterances()])))


print("Experiment B")
print("------------")

print("MAE_plan")
for plan in ['retrieval_plan', 'greedy_plan', 'ilp_plan']:
    print('\t{}: {:.2f}'.format(plan.upper(), np.mean([abs(estimate_perception(perception_models[utt.meta['receiver']], \
                            utt.meta[plan]) - utt.meta['intended_politeness']) for utt in ind_corpus.iter_utterances()])))
    
print("#-ADDED")
for plan in ['retrieval_plan', 'greedy_plan', 'ilp_plan']:
    print('\t{}: {:.2f}'.format(plan.upper(), \
                                np.mean([len(utt.meta[plan] - utt.meta['strategy_set']) for utt in ind_corpus.iter_utterances()])))
        
from strategy_manipulation import add_strategies_to_utt

# requires strategy marker annotations 
# and also an already computed plan, stored under "<plan_prefix>_plan"

def prepare_corpus_for_generation(corpus, plan_prefix):
    
    for utt in corpus.iter_utterances():
        
        plan = utt.meta["{}_plan".format(plan_prefix)]
        
        # strategies to remove
        strategies_to_remove = utt.meta['strategy_set'] - plan
        remove_strategies_from_utt(utt, strategies_to_remove, \
                                   removed_attribute_name="{}_context".format(plan_prefix))
        
        # strategies to be added 
        utt.meta['{}_addition'.format(plan_prefix)] = plan - utt.meta['strategy_set']
        
for mode in ['ilp', 'greedy', 'retrieval']:
    
    prepare_corpus_for_generation(mt_corpus, mode)
    prepare_corpus_for_generation(ind_corpus, mode)
    
for prefix in ['ilp', 'greedy', 'retrieval']: 

    for utt in tqdm(mt_corpus.iter_utterances()):
        
        add_strategies_to_utt(utt, utt.meta['{}_addition'.format(prefix)], ps, spacy_nlp, \
                          content_attribute_name='{}_context'.format(prefix), \
                          output_attribute_name="{}_paraphrase".format(prefix))
            
for prefix in ['ilp', 'greedy', 'retrieval']: 

    for utt in tqdm(ind_corpus.iter_utterances()):
        
        # receiver's perception model is used to select the output that minimizes the perception gap 
        add_strategies_to_utt(utt, utt.meta['{}_addition'.format(prefix)], ps, spacy_nlp, \
                              perception_model = perception_models[utt.meta['receiver']], \
                              content_attribute_name='{}_context'.format(prefix), \
                              output_attribute_name="{}_paraphrase".format(prefix))
            
paraphrases_mt = mt_corpus.get_attribute_table(obj_type="utterance", \
                                        attrs=['intended_politeness', 'ilp_paraphrase', 'greedy_paraphrase', 'retrieval_paraphrase'])
    
paraphrases_ind = ind_corpus.get_attribute_table(obj_type="utterance", \
                                        attrs=['intended_politeness', 'ilp_paraphrase', 'greedy_paraphrase', 'retrieval_paraphrase'])
    
# read the generated outputs directly 

paraphrases_mt = pd.read_csv('output/mt.tsv', sep='\t', index_col=0, na_filter=False)
paraphrases_ind = pd.read_csv('output/ind.tsv', sep='\t', index_col=0, na_filter=False)


def compute_mae(df, col_name, perception_models, \
                politeness_transformer, spacy_nlp, \
                intended_col = 'intended_politeness', receiver_col = 'receiver'):
    
    # compute strategies present in each paraphrases
    annotated_utts = [politeness_transformer.transform_utterance(text, spacy_nlp) for text in df[col_name]]
    
    strategy_sets = [{k for k,v in utt.meta['strategies'].items() if v == 1} for utt in annotated_utts]
    receivers = df[receiver_col]
    
    # obtain perceived politeness with strategy set by the receiver 
    perceived_politeness = [estimate_perception(perception_models[receiver], strategies) \
                        for receiver, strategies in zip(receivers, strategy_sets)]
    
    return abs(df['intended_politeness'] - perceived_politeness)

print("Experiment A")
print("------------")

print("MAE_gen")

results_a = defaultdict()

for col in ["retrieval_paraphrase", 'greedy_paraphrase', 'ilp_paraphrase']:
    
    results_a[col] = compute_mae(paraphrases_mt, col, perception_models, ps, spacy_nlp)
    
    print("\t{}: {:.2f}".format(col.upper(), np.mean(results_a[col])))
    
print("Experiment B")
print("------------")

print("MAE_gen")

results_b = defaultdict()

for col in ["retrieval_paraphrase", 'greedy_paraphrase', 'ilp_paraphrase']:
    
    results_b[col] =  compute_mae(paraphrases_ind, col, perception_models, ps, spacy_nlp)
    
    print("\t{}: {:.2f}".format(col.upper(), np.mean(results_b[col])))
    
from scipy.stats import ttest_ind

print("Experiment A")
for baseline in ["retrieval", 'greedy']:
    stats, pval = ttest_ind(results_a['ilp_paraphrase'], results_a["{}_paraphrase".format(baseline)])
    print("\tpvalue for the diff between ilp and {}: {:.3f}".format(baseline, pval))

print()

print("Experiment B")
for baseline in ["retrieval", 'greedy']:
    stats, pval = ttest_ind(results_b['ilp_paraphrase'], results_b["{}_paraphrase".format(baseline)])
    print("\tpvalue for the diff between ilp and {}: {:.3f}".format(baseline, pval))
    
# add original texts to df 
paraphrases_mt['text'] = [mt_corpus.get_utterance(idx).text for idx in paraphrases_mt.index]
paraphrases_mt['back_translation'] = [mt_corpus.get_utterance(idx).meta['back_translation'] for idx in paraphrases_mt.index]

paraphrases_ind['text'] = [ind_corpus.get_utterance(idx).text for idx in paraphrases_ind.index]