import pandas as pd
import requests

df = pd.read_csv('bkash_banner3.csv')

image_url = df['Url'].head()

for img in image_url:
     file_name = img.split('/')[-1]
     print("Downloading file:%s"%file_name)
     r = requests.get(img, stream=True)
     
     with open(file_name, 'wb') as f:
            for chunk in r:
                  f.write(chunk)
