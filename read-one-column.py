import pandas as pd
import xlrd

df = pd.read_csv('bkash_banner3.csv')

p=df['Url'].head()

print(p)
