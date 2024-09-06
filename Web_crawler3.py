
import requests as rq
import json
import time
# from 모듈 명 import 해당 모듈의 함수명 > 모듈 명 없이 함수명으로만 사용가능 구문
from bs4 import BeautifulSoup as bs
from selenium import webdriver

html = """<html>
<head><title>Test site</title></head>
<body>
<div>
<p id = "i"  class ="a">Test1</p>
<p class ="d">Test2</p>
</div>
<p class ="d">Test3</p>
<a>a Tag</a>
<b>b Tag</b>
</body>
</html>"""

soup = bs(html, 'lxml')

# soup.태그 명 > 해당 태그의 정보를 가져옴
tag_p = soup.p
tag_span = soup.span
tag_title = soup.title
tag_body = soup.find_all('body')                    # find_all 메소드는 해당 값을 리스트에 형태로 반환 함
tag_p = tag_body[0].find_all("p")

# 리스트 형태로 인자 추가 시 여러 태그를 가져옴
# print(soup.find_all(["a","b","p"]))

# find_all 연속으로 사용하기
# print(type(tag_body), tag_body)
# print(type(tag_p), tag_p)

# find()는 하나의 요소만 가져옴 > ex) id 값을 찾을 시 유용
# print(soup.find("p"))
# print(type(soup.find("p")))
# print(soup.find_all("p"))
# # print(soup.find_all("p", limit=1))
# # print(soup.find_all("p", limit=1) [0])        # 리스트 형태로 반환하는 것이 아니라 일반 문자열?? 로 반환하는 차이가 있음
# print(soup.find_all("p") [0])
# print(soup.find("img"))


# select() 메소드 이용  > 리스트 형태로 반환함  > CSS 셀렉터를 이용하여 요소에 접근함 > p238쪽
# print(soup.select("p"))
# print(soup.select(".d"))        # class > 마침표, # > id로 표시함 
# print(soup.select("p.d"))       # 태그가 p 이면서 클래스가 d인 경우 
# print(soup.select("#i"))
# print(soup.select("p#i"))       # 태그가 p 이면서 id가 i인 경우  

# select() 메소드 연속으로 이용하기 > 태그와 태그 사이의 띄어쓰기로 자식태그를 표현함 
print(soup.select("body p"))
print(soup.select("body .d"))
print(soup.select("body p.d"))
print(soup.select("body #i"))
print(soup.select("body p#i"))
print(soup.select("div p"))

# extract()는 태그를 지우는 것 > style, script 등을 제거가능 
# 실질적으로는 제거하지 않음 
a = soup.body.extract()
print(a,"제거대상")
print(soup,"제거완료상태")
