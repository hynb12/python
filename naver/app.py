import requests
from bs4 import BeautifulSoup


def nowVal(code):
    data = requests.get(
        f'https://finance.naver.com/item/sise.naver?code={code}')  # 글자중간에 변수 넣기 >> f'글자{변수}글자'
    soup = BeautifulSoup(data.content, 'html.parser')
    print('====================================================')
    print('종목 : '
          + soup.select('div#middle div.wrap_company h2 a')[0].text+"("+code+")")
    print('현재가 : '+soup.find_all('strong', id="_nowVal")[0].text)
    print('거래량 : '+soup.find_all('span', class_="tah")[5].text)
    return soup.find_all('strong', id="_nowVal")[0].text+'\n'


# nowVal('005930')
# nowVal('066570')
# nowVal('000660')

homework = ['005930', '066575', '005380', '307870', '034220', '003490']

f = open('b.txt', 'w')
for i in homework:
    f.write(nowVal(i))     
f.close()
