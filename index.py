import requests
from bs4 import BeautifulSoup

def get_per(code):
    url = f"https://finance.naver.com/item/main.nhn?code={code}"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    per = soup.select("#_per")[0].text
    return float(per)

print(get_per("000660")) # SK 하이닉스 PER 값
print(get_per("005930")) # 삼성전자 PER 값