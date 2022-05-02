from libs.naver.NaverShopping.crawler import crawl
from libs.naver.NaverShopping.parser import parse


pageString = crawl('')

products = parse(pageString)

print(products)

