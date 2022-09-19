import requests
import bs4
from datetime import datetime

html = requests.get('http://www.paullab.co.kr/stock.html')

# print(html.text)

# html.headers

# html.encoding

html.encoding='utf-8'

print(html.text) # html 내용이 잘 나옴.

print(html.status_code) # 200

print(html.ok) # True

#---------------------------

import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettyify()) # html을 문서 형식으로 이쁘게 출력해준다.

# 근데 그래도 보기 힘들어서 그냥 파일로 내려받자.

f = open('test.html', 'w', encoding='utf-8')
f.write(html) # 여기의 html은 위의 response.text를 받음.
f.close()

# 이걸 텍스트 에디터로 열자.
# 이렇게 하면, 텍스트 에디터에서 제공하는 여러 기능, 모듈을 사용할 수 있다.

# -------------------------------
# crawling.

s = html.split(' ') # 띄어쓰기로 구분
word = input('페이지에서 검색할 단어를 입력하세요: ')
s.count(word)

s.count('...') # 특정 문자열 개수 세기

# 근데, 띄어쓰기로 구분했으므로, 특정 문자열 앞뒤에 띄어쓰기가 안되어있으면
# 구분을 못해서, counting이 안되는 문제 발생!

# 여기서 BeautifulSoup의 장점.
# <str타입의 html 데이터르 html 구조를 가진 데이터로 가공해주는 라이브러리>

#---------
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 이제 이거를..

print(soup.title) # <title>Document</title>
print(soup.title.string) # Document
print(soup.tr(임의의 태그)) # 처음 만나는 그 태그를 출력!!!

# 메서드로 접근할수도 있음.
print(soup.find('title')) # <title>Document</title>
print(soup.find('tr'))

print(soup.find(id=('update')))
print(soup.find('head').find('title'))

print(soup.find('h2', id='제주코딩베이스캠프연구원'))

print(soup.find_all('h2')) # 리스트로 리턴해줌