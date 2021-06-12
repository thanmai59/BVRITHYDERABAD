# -*- coding: utf-8 -*-


import json
import spacy
from collections import defaultdict

from convokit import Corpus, Utterance, Speaker
from convokit import download
from convokit import PolitenessStrategies, TextParser

# you will need to update the path of the downloaded/trained model in settings.py first
from strategy_manipulation import remove_strategies_from_utt, add_strategies_to_utt

# we use spacy to obtain parses for text, which the strategy extractor rely on 
spacy_nlp = spacy.load('en_core_web_sm', disable=['ner'])

# we use politeness strategy collection "politeness_local", 
# i.e., a subset of strategies that can be achieved through localized markers   
ps = PolitenessStrategies(strategy_attribute_name="strategies", \
                          marker_attribute_name="markers", \
                          strategy_collection="politeness_local")
    
message = "Is this page really still a stub?  Seems like enough information to remove the stub marker."

strategy_plan = {"Subjunctive", "For.Me", "Gratitude"}

def edit_utterance_by_plan(message, strategy_plan, spacy_nlp, politeness_transformer):
    
    # importantly, we need to have markers set to be true to know the exact positions of the markers for later edits
    utt = politeness_transformer.transform_utterance(message, markers=True)

    # strategies currently used
    strategy_set = {k for k,v in utt.meta['strategies'].items() if v == 1}
    
    utt.meta['strategy_set'] = strategy_plan
    
    # We can then determine strategies that needs to be deleted, as well as strategies that should be added, by comparing strategy_plan and strategy_set.
    to_delete = strategy_set - strategy_plan
    to_add = strategy_plan - strategy_set
    
    remove_strategies_from_utt(utt, to_delete, removed_attribute_name='context')
    
    return add_strategies_to_utt(utt, to_add, politeness_transformer, spacy_nlp)

edit_utterance_by_plan(message, strategy_plan, spacy_nlp, ps)

for intended_politeness in range(-1, 3):
    
    print("Intended politeness level = {}".format(intended_politeness))
    

# load average perception model 
from settings import PERCEPTION_MODEL_PATH
from plan_with_ilp import get_ilp_solution
with open(PERCEPTION_MODEL_PATH, 'r') as f:
    AVERAGE_MODEL = json.load(f)
def paraphrase_utterance_by_intention(message, intended_politeness, spacy_nlp, politeness_transformer, perception_model = AVERAGE_MODEL):
    
    # importantly, we need to have markers set to be true to know the exact positions of the markers for later edits
    utt = politeness_transformer.transform_utterance(message, markers=True)

    # strategies currently used
    strategy_set = {k for k,v in utt.meta['strategies'].items() if v == 1}
    
    utt.meta['strategy_set'] = strategy_set
    utt.meta['intended_politeness'] = intended_politeness
    strategy_plan = get_ilp_solution('0', strategy_set, perception_model, perception_model, set(), intended_politeness=intended_politeness)
    print('Recommended strategy plan:', strategy_plan)
    
    to_delete = strategy_set - strategy_plan
    to_add = strategy_plan - strategy_set
    
    remove_strategies_from_utt(utt, to_delete, removed_attribute_name='context')
    
    return add_strategies_to_utt(utt, to_add, politeness_transformer, spacy_nlp)
    

for intended_politeness in range(-1, 3):
    
    print("Intended politeness level = {}".format(intended_politeness))

    print(paraphrase_utterance_by_intention(message, intended_politeness, spacy_nlp, ps))
    print()