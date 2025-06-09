import requests
from bs4 import BeautifulSoup
import urllib.request  # import 모여있는 맨위에다가 작성

data = requests.get('https://finance.naver.com/item/main.nhn?code=005930')

print(data.content)
print(data.status_code)  # 접속 제대로 되고 있나 확인 가능(200)

# 내용을 예쁘게 만들어줌
soup = BeautifulSoup(data.content, 'html.parser')

# 찾은 결과는 []로 뱉어줌(list), find_all(태그명, 속성명)
print(soup.find_all('span', id="time")[0].text)

# 1. 'class'로 찾고싶으면 'class_'
# 2. 띄어쓰기로 여러개 있으면 하나만 쓰기
print(soup.find_all('p', class_="no_today")[0].text)

# 태그명은 그냥 이름만 쓰기, 내부 요소를 찾으려면 띄어쓰기
print(soup.select('em.f_down span'))
print(soup.select('#rate_info_nxt > div > p.no_today > em > span:nth-child(6)'))

image = soup.select('#img_chart_area')[0]
print('image : '+str(image))

imageSrc = image['src']
print('imageSrc : '+imageSrc)  # 이미지 속성값만 받기

# 이미지 URL을 알고있을 때 파일로 저장하는 법
urllib.request.urlretrieve(imageSrc, '이미지.jpg')
