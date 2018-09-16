#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2} # 不加载图片
chrome_opt.add_experimental_option("prefs",prefs)
# chrome_opt.add_argument('--headless')
# chrome_opt.add_argument('--disable-gpu')
# chrome_opt.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"')
driver = webdriver.Chrome(executable_path = DRIVER_BIN, chrome_options=chrome_opt)
driver.set_page_load_timeout(30)

f = open('/Users/vector/Desktop/crawler/urls.txt')
indexFile = open('/Users/vector/Desktop/crawler/now.txt')
results = []
lines = f.readlines()
inow = indexFile.readline().strip('\n')
# print inow
now = int(inow) + 1

tmpf = open('/Users/vector/Desktop/crawler/tmps.txt')
results = tmpf.readlines()
# print results


def hasBefore(line):
    for item in results:
        if item.startswith(line):
            return item
    return None

for index in range(now, len(lines)):
    line = lines[index]
    line=line.strip('\n')
    before = hasBefore(line)
    if before:
        with open('/Users/vector/Desktop/crawler/now.txt','w')as fm:
            fm.write(str(index))
        print before.strip('\n')
        results.append(before)
    else:
        try:
            driver.get(line)
        except TimeoutException:
            pass
        finally:
            with open('/Users/vector/Desktop/crawler/now.txt','w')as fm:
                fm.write(str(index))
            print line, driver.title
            results.append(line + " " + driver.title)
            # driver.execute_script('window.stop()')
driver.close()
# print results
