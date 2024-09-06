
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
html = """<html><head><title>Test site</title></head><body><p><a>TEST1</a><b>TEST2</b><c>TEST3</c</p></body></html>"""
soup = bs(html,'lxml')


# soup.태그 명 > 해당 태그의 정보를 가져옴  
tag_title = soup.title
tag_p = soup.p
tag_span = soup.span
tag_title = soup.title


# text vs string 
data_text = tag_p.text                  # text의 경우 p태그 하위의 태그 값도 가져옴 
# data_string = tag_p.string              # string의 경우 p태그 하위의 태그 값도 가져오지 못함 
# data_string2 = tag_p.span.string        # string의 경우 하위 태그도 명시해줘야 함  > 해당 자식 태그의 첫번째 값을 가져옴 

print("data_text > ",data_text,type(data_text))
# print("data_string > ",data_string,type(data_string))
# print("data_text > ", data_text,type(data_text))
# print("data_string > ", data_string,type(data_string))
# print("data_string > ", data_string2,type(data_string2))

#자식태그 접근하기 
# tag_p_children = soup.p.contents                  
# tag_p_children2 = soup.p.children                 # children의 경우 iterator object 형태로 반환 됨  > 반복문을 이용 함  

# print(tag_p_children)
# print(tag_p_children2)


# for child in tag_p_children2:
#     print(child)

# 부모태그 접근하기 
# tag_span_parent = tag_span.parent
# tag_title_parent = tag_title.parent
# tag_span_parents = tag_span.parents     #parents 사용 시 최상위 부모 태그까지 값을 가져옴
# tag_title_parents = tag_title.parents

# print(tag_span_parent)
# print(tag_title_parent)
# print(tag_span_parents)
# print(tag_title_parents)

# for span_parents in tag_span_parents:
#     print(span_parents)

# for title_parents in tag_title_parents:
#     print(title_parents)

# 형제태그 접근  > next_siblings , previous_siblings 
# a = tag_span.next_sibling
# b = a.previous_sibling
# tag_a = soup.a
# tag_b = soup.b
# tag_c = soup.c

# # print(a)
# # print(b)
# print(tag_a)
# print(tag_b)
# print(tag_c)

#다음, 이전 요소 접근하기 
# tag_a = soup.a
# tag_a_nexts = tag_a.next_elements
# tag_c = soup.c
# tag_c_previous = tag_c.previous_elements

# for i in tag_c_previous:
#     print(i)

#print(soup.prettify())