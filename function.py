import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from math import nan
import re
import os
import sys
from unicodedata import category
from time import sleep
import datetime
import pandas as pd
from openpyxl.workbook import Workbook
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as bs4
from html_table_parser import parser_functions as parser
import collections
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable
import json

# 절대 경로
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(relative_path)))
    return os.path.join(base_path, relative_path)

# 크롬 경로
chrome_exe = resource_path('chromedriver.exe')

# 크롬 옵션
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("start-maximized")
options.add_argument("--disable-software-rasterizer")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")


# step 0 - 카테고리 데이터 받아오기
def step0(link):
    response = requests.get(link)
    html = response.text
    bs4(html, 'html.parser')
    soup.find_all(...)

    return 0


# step 1 - 기본적인 상품 데이터를 크롤링하는 함수
def step1(link, category, sort, count):

    # 1. 크롤링 입장
    driver = webdriver.Chrome(executable_path=chrome_exe, chrome_options=options)
    driver.get(url=link)

    # 2. 크롤링 활동.
    driver.find_element(By.XPATH, ...)

    # 해당하는 링크(count 수만큼) 차곡차곡 정리하기
    html = driver.page_source
    soup = bs4(html, 'html.parser')

    return 0


# step 2 - 기존 내용(csv 파일 저장)인 AS 전화번호, AS 안내내용, 판매가 추가금액 -> 데이터 프레임에 추가하는 함수
def step2(df):
    return df


# step 3 - 기존 내용(csv 파일 저장)을 바탕으로, 금지어로 필터링 함수
def step3(df):
    return df


# step 4 - 기존 내용(csv 파일 저장)을 바탕으로, HTML 변환해서 데이터 프레임에 넣어주는 함수
def step4(df):
    return df


# 이미지 폴더 저장/엑셀 저장
def final(df, location):

    # image folder 저장
    os.makedirs(f"{location}/result")
    for i in range(len(df)):
        imgUrl = df['대표_이미지_파일명'][i]
        imgName = df['상품명'][i]
        with urlopen(imgUrl) as f:
            with open(f"{location}/result/{imgName}.jpg",'wb') as h: # 이미지 + 사진번호 + 확장자는 jpg
                img = f.read() #이미지 읽기
                h.write(img) # 이미지 저장

    # 대표_이미지_파일명 변경
    df['대표_이미지_파일명'] = df['상품명'].copy()

    # file 저장
    save_xlsx = pd.ExcelWriter(f"{location}/result.xlsx")
    df.to_excel(save_xlsx, index = False) # xlsx 파일로 변환
    save_xlsx.save() #xlsx 파일로 저장

# step 5 - HTML 코드 관리부분을 py에서 수정하는 함수(결국 csv 수정하는 느낌으로)
def replace_html(up, html, down):
    html_df = pd.DataFrame([[up, html, down]], columns=['상단이미지','html','하단이미지'])
    html_df.to_csv(resource_path('html.csv'))


# step 6 - A/S 부분 수정하는 함수
def replace_as(number, info, sale, sale_method):
    as_df = pd.DataFrame([[number, info, sale, sale_method]], columns=['A/S 전화번호','A/S 안내내용','판매가 추가','방식'])
    as_df.to_csv(resource_path('as.csv'))

# step 8 - 금지어 수정하는 함수
def replace_ban(ban_list):
    ban_df = pd.DataFrame(ban_list, columns=['금지어'])
    ban_df.to_csv(resource_path('ban.csv'))

# step 7 - 생성된 데이터 프레임에서, 사용자가 원하는 행을 삭제하도록 하는 함수
def remove_row(df, row_list):
    df.drop(row_list,inplace=True)
    df.reset_index(drop=True,inplace=True)

    # 최종 결과물 전달
    return df

# step 8 - 코드 입력 시 맞는지 확인 함수
def code_avail(code):
    code_df = pd.read_csv(resource_path('code.csv'))
    code_list = code_df['code'].tolist()
    if code in code_list:
        return True