import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("en.openfoodfacts.org.products.tsv", sep='t', low_memory=False)

