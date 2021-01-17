import requests

image_url = [
  "https://vision-images-store.s3.amazonaws.com/internship/zipper/view_1/3213e9e9da734c268db6bed4b76ea411.jpg",
  "https://vision-images-store.s3.amazonaws.com/internship/zipper/view_1/3a4e9c2704bb46afb5a43c3231974e04.jpg",
  "https://vision-images-store.s3.amazonaws.com/internship/zipper/view_1/48d93cb06ede452fbab83495a4ff17a6.jpg",
  "https://vision-images-store.s3.amazonaws.com/internship/zipper/view_1/c7d91a112c6341eb84ed8e62ea4d6aa8.jpg",
  "https://vision-images-store.s3.amazonaws.com/internship/zipper/view_1/5cb6f2cdd3a244af9d9640be6e65b4f0.jpg",
  "https://vision-images-store.s3.amazonaws.com/internship/zipper/view_1/b5804b834f2945dabd87892df695f5b2.jpg",
  "https://vision-images-store.s3.amazonaws.com/internship/zipper/view_1/c1a05e6fa0b24a2490b10b80760dae83.jpg"
]
for img in image_url:
 file_name = img.split('/')[-1]
 print("Downloading file:%s"%file_name)
 r = requests.get(img, stream=True)
 # this should be file_name variable instead of "file_name" string
 with open(file_name, 'wb') as f:
    for chunk in r:
       f.write(chunk)
