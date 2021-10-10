import urllib.request as req
from bs4 import BeautifulSoup
import requests
import settings

line_url = "https://notify-api.line.me/api/notify"
headers = {"Authorization": "Bearer " + settings.TOKEN}
message = ''
# https://qiita.com/Brutus/items/0a2e8d0c682d10c65a03
for url in settings.urls:
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "lxml") 
    
    train = soup.select_one("#main > div.mainWrp > div.labelLarge > h1").text
    status = soup.select_one("#mdServiceStatus > dl > dt").text
    info = soup.select_one("#mdServiceStatus > dl > dd > p").text 
    message += train+'\n'+status+'\n'+info

    # print(message)
payload = {"message": message}
requests.post(line_url, headers=headers, data=payload)
