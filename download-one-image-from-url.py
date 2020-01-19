import requests

r = requests.get("http://pic1.to8to.com/case/day_120720/20120720_fb680a57416b8d16bad2kO1kOUIzkNxO.jpg")
if r.status_code == 200:
    with open("test.jpg", "wb") as f:
        f.write(r.content)