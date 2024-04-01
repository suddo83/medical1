import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

# 주식 검색어 순위가 포함된 부분을 찾습니다
stock = soup.find('div', {'class': 'box_type_l'})

# 주식 검색어 순위 목록을 가져옵니다
stock_list = stock.find_all('a', {'class': 'tltle'})

# 검색어 출력
for item in stock_list:
    if "삼성전자" in item.text.strip():
        print(item.text.strip())




