# requests import
# 말그대로 원하는 url에서 데이터를 뽑아오는 기능
import requests

# 크롤링 기능 생성 keyword로 검색가능 구현 예정
def crawl(keyword):

    # 크롤링할 대상 url .. query 뒷부분에 키워드 대입 구현 예정
    url = "http://search.danawa.com/dsearch.php?k1=RTX%203050"

    # 상단의 url에서 데이터를 받아옴
    data= requests.get(url)

    # url에서 데이터를 잘받아왔는지 확인하기 위해 status_code 받아와서 출력. 200이면 정상, url도 똑바로 불러왔는지 확인
    print(data.status_code, url)


    return data.content
