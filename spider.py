# -*- codeing = utf-8 -*-
# Author: Redcomet
# QQ: 626206333
# @Time :2022/1/19 9:20
# @Author: Administrator
# @File :t1.py

from bs4 import BeautifulSoup              #beautiful soup4
import re               #正则
import urllib.request,urllib.error
import xlwt             #excel操作
import sqlite3          #进行sqlite3操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1. 爬取网页

    #2. 解析数据

    #3. 保存数据

# 爬取网页
def getData(baseurl):
    datalist = []
    return datalist
