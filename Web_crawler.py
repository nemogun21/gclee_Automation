
import requests as rq
import json
import time

from bs4 import BeautifulSoup as bs # from 모듈 명 import 해당 모듈의 함수명 > 모듈 명 없이 함수명으로만 사용가능 구문 
from selenium import webdriver


# url  = "https://pjt3591oo.github.io/"
# url  = "https://blog.naver.com/pjt3591oo"

# print(res.status_code)
# print(res.headers)

# headers = res.headers

# print(headers['Set-Cookie'])

# for header in headers:
#    print(headers[header])

# cookies = res.cookies
# print(list(cookies))
# print(dict(cookies))

# print(res.text)
# print(res.content)
# print(res.encoding)

# 쿼리스트링 데이터 만들어 요청 시 > params 를 이용
# res = rq.get(url,params={"key1":"value1","key2":"value2"})

# post 요청 시  > body 안에 데이터를 추가 할 경우 > data 를 이용

# url = "http://www.example.com"
# url = "//www.example.com"

# # 하기와 같이 post 요청 시 정상적으로 데이터 전달이 안될 수 있음 > json 모듈을 사용하여 이슈 제거 
# res = rq.post(url,data={"key1":"value1","key2":"value2"})
# print(res.url)

# # json 모듈을 사용
# res = rq.post(url,data=json.dumps({"key1":"value1","key2":"value2"}))
# print(res.url)

# exception 예외처리 방법 
# tip > 예외처리 시 프론트 단에서 처리 가능한 것을 제외하고 서버에서 에러나는 것등을 예외처리 할 것을 권장함 

# try :

#     res = rq.get(url)
#     print(res)

# except rq.exceptions.HTTPError:
#     print("HTTP error !!")

# except rq.exceptions.Timeout:
#     print("Timeout error !!")

# # url에 http or https를 적지 않음

# except rq.exceptions.MissingSchema:
#     print("MissingSchema error !!")
   
#selenium 이용
# delay_time = 13
# driver = webdriver.Chrome('chromedriver.exe')
# time.sleep(delay_time)

# bs4 학습 > bs4 설치 완료 함 

# html = """<html><head><title>Test site</title></head><body><p>TEST</p><p>TEST1</p><p>TEST2</p></body></html>"""
html = """<html><head><title class="t" id="ti">Test site</title></head><body><p>TEST</p><p>TEST1</p><p>TEST2</p></body></html>"""
soup = bs(html,'lxml')
tag_title = soup.title

# print('1',soup)
# print('2',tag_title)
# print('3',type(tag_title))
# print('4',type(soup))
# print('5',soup.prettify())
# print('6',tag_title.text)
# print('7',tag_title.string)
# print('8',tag_title.name)

# 타입이 bs4.element.Tag 인 경우 속성을 딕셔너리 처럼 접근가능 
# 딕셔너리 형태이기 때문에 딕셔너리 문법적용이 가능함 
print('9',tag_title.attrs)                      # 해당 태그의 모든 속성을 가져옴 
print('10',tag_title['class'])
print('10.1',tag_title.get('class'))
# print('11',tag_title['class1'])               # 문서 내 없는 속성값이 없을 경우 keyError 발생 > get() 이용하여 에러를 방지함  
print('12',tag_title.get('class'))
print('13',tag_title.get('id'))
print('14',tag_title.get('class1'))
print('15',tag_title.get('class1','default_value'))


