import pandas as pd
file_path = 'en.openfoodfacts.org.products.cvs'
df = pd.read_cvs(file_path, sep='\t', usecols=['product_name', 'categories', 'labels', 'ingredients_text'], low_memory=False)

df_us = df[df['countries'].str.contains('United States', na=False)]
df