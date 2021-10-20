import requests as rq              # request; a module that helps you interact with urls
from bs4 import BeautifulSoup 


url = "https://jumia.com/men-sneakers/"
headers = rq.utils.default_headers()
headers.update(
    {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36"}
)

res = rq.get(url, headers) 
print(res.status_code)                # res; my response
