import pandas as pd

df = pd.read_csv('bkash_banner3.csv')
p = df[['Url','result']].head()
print(p)
