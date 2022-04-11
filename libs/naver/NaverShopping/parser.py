# 뽑아온 데이터에서 원하는 데이터만 뽑아내는 기능구현

from bs4 import BeautifulSoup


def getProductInfo(li):
    print(li)
    productPrice = li.find("a", {"class":"click_log_product_standard_price_"})
    productName = li.find("p", {"class":"click_log_product_standard_title_"})
    realName = productName['title']
    realUrl = productName['href']

    return {"Name":realName, "Price":productPrice.text, "URL":realUrl}

def parse(pageString):

    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul", {"class":"product_list"})
    lis = ul.findAll("li", {"class":"prod_item "})

    products = []
    for li in lis:
        product = getProductInfo(li)
        products.append(product)
    return products

    return []