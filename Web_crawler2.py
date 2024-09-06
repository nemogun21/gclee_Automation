
import requests as rq
import json
import time
from bs4 import BeautifulSoup as bs # from 모듈 명 import 해당 모듈의 함수명 > 모듈 명 없이 함수명으로만 사용가능 구문 
from selenium import webdriver


# url  = "https://pjt3591oo.github.io/"
# url  = "https://blog.naver.com/pjt3591oo"

# bs4 학습 > bs4 설치 완료 함 

# html = """<html><head><title>Test site</title></head><body><p>TEST</p><p>TEST1</p><p>TEST2</p></body></html>"""
# html = """<html><head><title class="t" id="ti">Test site</title></head><body><p><span>TEST1</span><span>TEST2</span></p></body></html>"""
# html = """<html><head><title>Test site</title></head><body><p><a>TEST1</a><b>TEST2</b><c>TEST3</c</p></body></html>"""
# html = """<html><head><title>Test site</title></head><body><p><a>TTT<span>123</span><span>123</span></a><b>TEST2</b><c>TEST3</c</p></body></html>"""
# html = """<html><head><title>Test site</title></head><body><p>Test1</p><p>Test2</p><p>Test3</p></body></html>"""
html = """<html><head><title>Test site</title></head><body><p>Test1</p><p id = "d">Test2</p><p>Test3</p></body></html>"""

soup = bs(html,'lxml')

# soup.태그 명 > 해당 태그의 정보를 가져옴  
tag_title = soup.title
tag_p = soup.p
tag_span = soup.span
tag_title = soup.title

# 요소 접근하기 2 
# tag_p_nexts = soup.p.next_elements

# print(soup.prettify())
# print("elements")

# for i in tag_p_nexts:
#     print(i)

#요소 접근하기 3 !!!!   
print(soup.find_all("title"))
print(soup.find_all("p"))       # id 값은 패당 페이지에서 한 번만 사용가능 > 하나 또는 빈 리스트가 출력됨

# id 존재 유무로 태그 가져오기 
# print(soup.find_all(id = True))
# print(soup.body.find_all(id = False))         # 데이터 노출 범위를 body를 기준으로 함 
# print(soup.find_all(id = False))              # soup 자체가 문서 전체를 뜻하므로 필요없는 태그도 리스트로 노출 됨 
# print(soup.find_all("p",id = "d"))                
# print(soup.find_all("p",id = "c"))            # p 태그 중 id = c 인 값은 없음 
# print(soup.find_all("p",id = True))             # id 값의 존재유무로 값을 가져옴 

# # text 속성을 이용한 태그 찾기 
# print(soup.find_all("p", text = "Test1"))       # p 태그 안에 값이 Test1를 찾는 것  > text 는 값을 의미 함 

#limit 키워드를 이용한 태그 제한하기 
# print(soup.find_all("p", limit = 1))       
# print(soup.find_all("p", limit = 2))       

# find_all() 값이 없을 경우 문서의 모든 태그를 가져 옴 
