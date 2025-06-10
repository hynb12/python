import requests
from bs4 import BeautifulSoup


def nowVal(code):
    data = requests.get(
        'https://finance.naver.com/item/sise.naver?code='+str(code))
    soup = BeautifulSoup(data.content, 'html.parser')
    print('====================================================')
    print('종목 : '+soup.select('div#middle div.wrap_company h2 a')[0].text)
    print('현재가 : '+soup.find_all('strong', id="_nowVal")[0].text)
    print('거래량 : '+soup.find_all('span', class_="tah")[5].text)


nowVal('005930')
nowVal('066570')
nowVal('000660')
print('====================================================')
