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
    datalist = getData(baseurl)
    savePath = ""
    #2. 解析数据
    savePath = '\\豆瓣电影Top250.xls'
    #3. 保存数据
    saveData(savepath)

# 爬取网页
def getData(baseurl):
    datalist = []
    # 逐一解析数据
    return datalist

# 保存数据
def saveData(dbpath):
    print('save...')
