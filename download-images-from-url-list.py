import requests
path = "/media/user/A/github/python/image-downloader-from-csv/bkash_banner2.xlsx"
with open(path, 'r') as file1:
    text = file1.read()
    all_links = [i.strip() for i in file1.readlines()]
    j = 0
    imagename = f"Image{j}.jpg"
    for link in all_links:
        result = requests.get(link)
        if result.status_code == 200:
            try:
                image = result.raw.read()
                open(imagename, "wb").write(image)
            except Exception:
                pass
        else:
            pass
        j += 1

