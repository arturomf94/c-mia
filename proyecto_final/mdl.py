import pandas as pd
import numpy as np
from time import time
from pgmpy.estimators import ExhaustiveSearch
from pgmpy.models import BayesianModel
from pgmpy.estimators import BicScore
from pgmpy.estimators.BicScore import BicScore
inicio = time()
data = pd.read_csv('data.csv', sep=",", header=None)

searcher = ExhaustiveSearch(data, scoring_method=BicScore(data))
for score, model in searcher.all_scores():
    print("{0};{1}".format(score, model.edges()))
