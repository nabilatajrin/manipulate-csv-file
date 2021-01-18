import pandas as pd
import requests

df = pd.read_csv('bkash_banner3.csv')
image_url = df['Url'].head()

for img in image_url:
     file_name = img.split('/')[-1]
     file_path = r'/media/user/A/github/python/image-downloader-from-csv/images/%s'%file_name
     print("Downloading file:%s"%file_name)
     r = requests.get(img, stream=True)
    #download images
     with open(file_path, 'wb') as f:
            for chunk in r:
                  f.write(chunk)
