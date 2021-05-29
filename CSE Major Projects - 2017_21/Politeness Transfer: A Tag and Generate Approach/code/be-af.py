# -*- coding: utf-8 -*-


import pandas as pd
import os

from convokit import Corpus, Utterance, Speaker
from convokit import PolitenessStrategies
train_corpus = Corpus(filename=("data/train/training-corpus/"))
ps = PolitenessStrategies(strategy_attribute_name = "strategies", \
                          marker_attribute_name = "markers", \
                          strategy_collection="politeness_local")
# it is important to set markers to True
train_corpus = ps.transform(train_corpus, markers=True)

for utt in train_corpus.iter_utterances():
    
    strategy_split = utt.meta['strategy']
    assert utt.meta['strategies'][strategy_split] == 1
    
# helper functions further detailed in Marker_Edits.ipynb 
from strategy_manipulation import remove_strategies_from_utt

for utt in train_corpus.iter_utterances():
    
    remove_strategies_from_utt(utt, [utt.meta['strategy']])
    
utt = train_corpus.get_utterance('100087711.41.31')
#            100087711.41.31
#            10387534.0.0
#            105319599.26773.0

print("BEFORE:", utt.text)
print("AFTER:", utt.meta)
