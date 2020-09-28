import requests
from bs4 import BeautifulSoup

'''
def extract_url(url):
    if url.find("www.amazon.com") != -1:
        index = url.find("/dp/")
        if index != -1:
            url = "https://www.amazon.com" + url[index:index + 14]
        else:
            index = url.find("/gp/")
            if index != -1:
                url = "https://www.amazon.com" + url[index:index+22]
            else:
                url = None
    else:
        url = None
    return url
'''

'''
def get_converted_price(price):
    stripped_price = price.strip("$")
    replaced_price = stripped_price.replace(",", "")
    find_dot = replaced_price.find(".")
    to_convert_price = replaced_price[0:find_dot]
    converted_price = int(to_convert_price)

    return converted_price
'''


def get_product_details(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"}
    # details = {"name": "", "price": 0, "deal": True, "url": ""}
    # if url is None:
    #        details = None
    # else:
        # page holds the product's page
    page = requests.get(url, headers = headers)
    # soup holds the html
    soup = BeautifulSoup(page.content, "html5lib")
    find = soup.find("giờ trước")
    print(find)
    return find
    '''
    price = soup.find(id="newBuyBoxPrice")
    if price is None:
        details["deal"] = False
    if title is not None and price is not None:
        details["name"] = title.get_text().strip()
        details["price"] = get_converted_price(price.get_text())
        details["url"] = _url
    else:
        return None
    '''


inputString = input("Enter a product's URL: ")
print(get_product_details(inputString))
