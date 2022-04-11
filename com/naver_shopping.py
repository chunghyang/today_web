from libs.naver.NaverShopping.crawler import crawl
from libs.naver.NaverShopping.parser import parse

import json

pageString = crawl('')
products = parse(pageString)
print (products)
print (len(products))

file = open("./products1.json", "w+")
file.write(json.dumps(products))