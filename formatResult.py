#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('/Users/vector/Desktop/crawler/urlfull.txt')
tf = open('/Users/vector/Desktop/crawler/tmps_1.txt')
tf1 = open('/Users/vector/Desktop/crawler/tmps.txt')
result = open('/Users/vector/Desktop/crawler/results.txt','a')
lines = f.readlines()
tmps = tf.readlines()
tmps1 = tf1.readlines()

def hasBefore(line):
    for item in tmps1:
        if item.startswith(line):
            return item
    for item in tmps:
        if item.startswith(line):
            return item
    return line

for index in range(len(lines)):
    line = lines[index]
    line=line.strip('\n')
    a = hasBefore(line).strip('\n')
    result.write(a+'\n')

# print results
