import requests as rq              # request; a module that helps you interact with urls
from bs4 import BeautifulSoup as bs # scraping module


url = "https://jumia.com.ng/men-sneakers/"
headers = rq.utils.default_headers()
headers.update(
    {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36"}
)

res = rq.get(url, headers) # res; my response
first_soup = bs(res.content, features="lxml")  # using beautiful soup   
second_soup = first_soup.find("div", attrs={"class": "-paxs row _no-g _4cl-3cm-shs"})
soupList = second_soup.find_all("article", attrs= {"class": "prd _fb col c-prd"})

for soup in soupList:
    # print(soup.prettify())
    sneaker_details = soup.find("a")

    # the description
    sneaker_description = sneaker_details.get("data-name")

    # The old price
    try:
        old_div = soup.find("div", attrs = {"class": "old"})
        oldprice_raw = old_div.text
        sneaker_oldprice = int(oldprice_raw.lstrip('₦ ').replace(',', ''))  # or split('₦')[1]
    except:
        sneaker_oldprice = None

    # The new price
    break










# print(soupList)
# print(second_soup.prettify())
# print(res.status_code)
# print(first_soup)      


