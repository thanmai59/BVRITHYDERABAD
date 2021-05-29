# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import json
import os
import spacy
from collections import Counter
from tqdm import tqdm

import json
import spacy
from collections import defaultdict

from convokit import Corpus, Utterance, Speaker
from convokit import download
from convokit import PolitenessStrategies, TextParser

# you will need to update the path of the downloaded/trained model in settings.py first
from strategy_manipulation import remove_strategies_from_utt, add_strategies_to_utt

mt_corpus = Corpus(filename="data/test/mt-test-corpus")

mt_corpus.get_utterance('226408211.416.416').meta

ps = PolitenessStrategies(strategy_attribute_name = "strategies", \
                          marker_attribute_name = "markers", \
                          strategy_collection="politeness_local")

spacy_nlp = spacy.load('en', disable=['ner'])

# get politeness strategies for the back translations 
translated_strategies = {utt.id: ps.transform_utterance(utt.meta['back_translation'], \
                         spacy_nlp=spacy_nlp, markers=True) for utt in mt_corpus.iter_utterances()}
    
    
cnts = {'Subjunctive': 0, "Please": 0, 'Filler': 0, "Swearing": 0}

for utt in mt_corpus.iter_utterances():
    
    k = utt.meta['strategy']
    cnts[k] += translated_strategies[utt.id].meta['strategies'][k]

print("===Strategy Preservation Rate===")
for k, v in cnts.items():
    
    # counts are out of a total of 200 instances  
    print("{}: {:.1f}% ".format(k.upper(), v/2))
    
ind_corpus = Corpus(filename="data/test/ind-test-corpus/")

ind_corpus.get_utterance("A23-A3S-1").meta

pairs = [(utt.meta['sender'], utt.meta['receiver']) for utt in ind_corpus.iter_utterances()]

from collections import defaultdict
from perception_utils import scale_func, get_strategies_df, get_model_info, get_ind_model_info

wiki_politeness = Corpus(download("wikipedia-politeness-corpus"))

wiki_politeness = ps.transform(wiki_politeness, markers = False)

for utt in wiki_politeness.iter_utterances():
    
    utt.meta['avg_score'] = scale_func(np.mean(list(utt.meta['Annotations'].values())))
    
df_avg = get_strategies_df(wiki_politeness, 'strategies')
scores = [wiki_politeness.get_utterance(idx).meta['avg_score'] for idx in df_avg.index]

avg_model = get_model_info(df_avg, scores)
avg_model

turker_corpus = Corpus(filename="data/perceptions/turker-corpus/")

Counter([utt.speaker.id for utt in turker_corpus.iter_utterances()])

turker_corpus = ps.transform(turker_corpus, markers=True)

turkers = ['A23', 'A2U', 'A1F', 'A3S', 'AYG']
turker_dfs = defaultdict()

for turker in turkers:
    
    corpus = turker_corpus.filter_utterances_by(selector=lambda utt:utt.speaker.id == turker)
    
    df = get_strategies_df(corpus, "strategies")
    
    df['score'] = [corpus.get_utterance(idx).meta['score'] for idx in df.index]
    
    turker_dfs[turker] = df
    
avg_coefs = avg_model['coefs']

for t, df in turker_dfs.items():
            
    df_feat = df.iloc[:, 0:-1]
    scores = dict(df.iloc[:, -1])

    ind_model = get_ind_model_info(df_feat, scores, avg_coefs)     
  
    print(t)
    print(ind_model)
    print('======')