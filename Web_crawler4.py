
import requests as rq
import json
import time
import re       # Regular Expression > 정규식

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

# 메소드를 이용한 태그삭제 

# def remove_tag(soup,tags):
#     if tags == [] :
#         return False

    
#     removes = []

#     for tag in soup.find_all(tags):
#         removes.append(tag.extract())
#     return removes


# removed_tag = remove_tag(soup, [])                            # 해당 함수의 첫번재 인자는 문서전체이고, 두번재 인자는 제거하고 싶은 태그임 
# print(removed_tag)                                            # 빈[]인 경우 False 반환 
# print(soup)

# 정규식을 활용한 bs4 고급스킬 
print("1", soup.find_all(class_=re.compile("d"))) 
print("2", soup.find_all(id=re.compile("i"))) 
print("3", soup.find_all(re.compile("t"))) 
print("4", soup.find_all(re.compile("^t")))             # 태그 이름이 t로 시작하는 요소를 찾음  > ^ > 시작을 의미
print("5", soup.find_all(href = re.compile("/"))) 

