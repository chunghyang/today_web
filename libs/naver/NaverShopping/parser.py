# 뽑아온 데이터에서 원하는 데이터만 뽑아내는 기능구현

from bs4 import BeautifulSoup

def parse(pageString):

    bsObj = BeautifulSoup(pageString, "html.parser")

    goods_list = bsObj.select('li.prod_item')


    print(len(goods_list))

    return []