from urllib.request import urlopen								
from bs4 import BeautifulSoup								
import datetime								
import random								
import pymysql								
import re								
conn = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock',								
                        user='root', passwd='thuy', db='sof_question', charset='utf8')								
cur = conn.cursor()								
cur.execute("USE sof_question")								
def query(pageNumber, pageSize):								
        firstRecord = (pageNumber -1)* pageSize								
        maxRecord = pageSize								
        cur.execute('SELECT * FROM question LIMIT '+str(firstRecord)+','+str(maxRecord))								
        result = cur.fetchall()								
        for re in result:								
                print(re)								
try:								
        print("nhap so thu tu trang:")								
        a = int(input())								
        print("nhap so record trong trang")								
        b = int(input())								
        query(a,b)								
finally:								
                cur.close()								
                conn.close()								
