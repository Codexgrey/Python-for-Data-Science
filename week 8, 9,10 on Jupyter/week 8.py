import requests
from bs4 import BeautifulSoup
import csv


new_file = open("C:/Users/user/Desktop/DATA - SCIENCE/Python 101/week 8/jumia sneakers.csv", mode = "w", encoding = "utf-8", newline = "")
pen = csv.writer(new_file)
pen.writerow(["S|N", "description", "old price", "old lp", "old hp", "new price", "new lp", "new hp", "discount", "ratings"])

entire_data = []
index = 1


url = "https://jumia.com.ng/men-sneakers/"
headers = requests.utils.default_headers()
headers.update(
    {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
)


my_response = requests.get(url, headers)
first_soup = BeautifulSoup(my_response.content, features = "lxml")

second_soup = first_soup.find("div", attrs = {"class" : "-paxs row _no-g _4cl-3cm-shs"})

list_of_soups = second_soup.find_all("article", attrs = {"class" : "prd _fb col c-prd"}) 
# print(len(list_of_soups))



for soup in list_of_soups:
    sneaker_details = soup.find("a")

    ##THE DESCRIPTION
    try:
        sneaker_description = sneaker_details.get("data-name")
    except:
        sneaker_description = None
    
    ##THE OLD PRICE
    try:    #if there is an old price
        old_div = soup.find("div", attrs = {"class" : "old"})
        old_price_raw = old_div.text
        if "-" in old_price_raw:    #if there is a range
            old_lp = int(old_price_raw.split(" - ")[0].lstrip("₦ ").replace(",", "")) #lp - low price
            old_hp = int(old_price_raw.split(" - ")[1].lstrip("₦ ").replace(",", "")) #hp - high price
            sneaker_old_price = None
        else:    #if there is a single price
            sneaker_old_price = int(old_price_raw.lstrip("₦ ").replace(",", ""))
            old_lp = None
            old_hp = None
    except:     
        sneaker_old_price = None
        old_lp = None
        old_hp = None

    ##THE NEW PRICE
    try:
        new_div = soup.find("div", attrs = {"class" : "prc"})
        new_price_raw = new_div.text
        if "-" in new_price_raw:
            new_lp = int(new_price_raw.split(" - ")[0].lstrip("₦ ").replace(",", ""))
            new_hp = int(new_price_raw.split(" - ")[1].lstrip("₦ ").replace(",", ""))
            sneaker_new_price = None
        else:
            sneaker_new_price = int(new_price_raw.lstrip("₦ ").replace(",", ""))
            new_lp = None
            new_hp = None
    except:
        sneaker_new_price = None
        new_lp = None
        new_hp = None

    #FOR SNEAKER DISCOUNT
    try:
        discount_div = soup.find("div", attrs = {"class" : "tag _dsct _sm"})
        sneaker_discount = discount_div.text
    except:
        sneaker_discount = None
    
    #FOR SNEAKER RATING
    try:
        rating_div = soup.find("div", attrs = {"class" : "stars _s"})
        rating_phrase = rating_div.text
        sneaker_rating = float(rating_phrase.split(" ")[0])
    except:
        sneaker_rating = None

    entire_data.append([index, sneaker_description, sneaker_old_price, old_lp, old_hp, sneaker_new_price, new_lp, new_hp, sneaker_discount, sneaker_rating])
    index += 1


pen.writerows(entire_data)
new_file.close()
