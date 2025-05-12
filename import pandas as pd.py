import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("en.openfoodfacts.org.products.tsv", sep='t', low_memory=False)
df_us = df[df["countries_tags"].str.contains("en:united-states", na=False)]
df_us = df_us[df_us["categories_tags"].notnull()]

G = nx.DiGraph()
for category_list in df_us["categories_tags"]:
    for i in range(len(categories) - 1):
        parent = categories[i].strip().replace("en:", "").replace("-", " ").title()
        child = categories[i + 1].strip().replace("en:", "").replace("-", " ").title()
        

