
import requests as rq
import json
import time
import re       # Regular Expression > 정규식

# from 모듈 명 import 해당 모듈의 함수명 > 모듈 명 없이 함수명으로만 사용가능 구문
from bs4 import BeautifulSoup as bs
from selenium import webdriver

# base_url = "https://pjt3591oo.github.io/"
# page_path = "/page%d"
# page = 2 

# res = rq.get(base_url)

# soup = bs(res.content, 'lxml')

# posts = soup.select("body main.page-content div.wrapper div.home div.p")

# print(posts)

# for post in posts:                              # text의 경우 대상 태그 하위의 태그 값도 가져옴
#         title = post.find("h3").text.strip()        
#         descript = post.find("h4").text.strip()        
#         author= post.find("span").text.strip()        
#         print("1", title)
#         print("2", descript)
#         print("3", author)
#         print("PAGE1")

# #--------------------------------------------------- > 위에 코드만 사용 시 1페이지만 값을 가져옴 

# while True:
#     sub_path = page_path%(page)
#     # page = page + 1
#     page +=1
#     print("PAGE",page)

#     res = rq.get(base_url + sub_path)

#     if (res.status_code != 200):
#         break
        
#     soup = bs(res.content, 'lxml') 

#     posts = soup.select("body main.page-content div.wrapper div.home div.p")

#     for post in posts:                              # text의 경우 대상 태그 하위의 태그 값도 가져옴
#         title = post.find("h3").text.strip()        
#         descript = post.find("h4").text.strip()        
#         author= post.find("span").text.strip()        
#         print("1", title)
#         print("2", descript)
#         print("3", author)


#-----------------------------------------------------------------------------------------------------------------------------
# 메소드를 사용하여 코드개선 하기 

def get_posts(soup):
    return soup.select("body main.page-content div.wrapper div.home div.p")   # 띄어쓰기 자식태그로 이동 , (.)은 class 나타냄, #은 id 나타냄 

def data_parse(posts):
    for post in posts:                              # text의 경우 대상 태그 하위의 태그 값도 가져옴
        title = post.find("h3").text.strip()        # strip() > 양쪽공백을 지움 > 점프 투 파이썬 p70 
        descript = post.find("h4").text.strip()        
        author= post.find("span").text.strip()        
        print("1", title)
        print("2", descript)
        print("3", author)

base_url = "https://pjt3591oo.github.io/"
page_path = "/page%d"
page = 2 

res = rq.get(base_url)

soup = bs(res.content, 'lxml')

posts = get_posts(soup)
data_parse(posts)

while True:
    sub_path = page_path%(page)
    # page = page + 1
    page +=1
    print("PAGE",page)

    res = rq.get(base_url + sub_path)

    if (res.status_code != 200):
        break
        
    
    soup = bs(res.content, 'lxml') 

    posts = get_posts(soup)
    data_parse(posts)



