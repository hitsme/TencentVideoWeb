#!/usr/bin/python3
# encoding: utf-8
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import json
import time
import sys
import io
DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0"}
DEFAULT_TIMEOUT = 360
def getBrowser():
  browser = webdriver.Firefox()
  browser.set_page_load_timeout(5)
  try:
     browser.get('https://v.qq.com/')
  except TimeoutException:
      browser.execute_script("window.stop()")
  with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())

  for cookie in listCookies:
    # fix the problem-> "errorMessage":"Unable to set Cookie"
      for k in ('name', 'value', 'domain', 'path', 'expiry'):
        if k not in list(cookie.keys()):
            if k == 'expiry1':
                t = time.time()
                cookie[k] = cookie[k] # 时间戳 秒
    # fix the problem-> "errorMessage":"Can only set Cookies for the current domain"
      browser.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path', 'expiry') if k in cookie})

  #browser.get("https://v.qq.com/x/cover/m441e3rjq9kwpsc/m00253deqqo.html")
  #time.sleep(5)
  #browser.save_screenshot('test.png')
  #html = browser.execute_script("function m3u8print(){this._m3u8 = PLAYER._DownloadMonitor.context.dataset.currentVideoUrl;console.log(_m3u8);return _m3u8;}return m3u8print();")
  #sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
  #print(str(html))
  return browser

    #while True:
     #vurl=input("输入你视频链接：\n")
     #browser.get(vurl)
     #time.sleep(3)
     #print(browser.execute_script("function m3u8print(){this._m3u8 = PLAYER._DownloadMonitor.context.dataset.currentVideoUrl;console.log(_m3u8);return _m3u8;}return m3u8print();"))
     #browser.get("https://v.qq.com")

browser=getBrowser()


def getYourVideoUrl(browser, yourVideoUrl):
    print(yourVideoUrl)
    try:
      browser.get(yourVideoUrl)
      time.sleep(3)
    except TimeoutException:
        browser.execute_script("window.stop()")
    videoUrl=browser.execute_script(
     "function m3u8print(){this._m3u8 = PLAYER._DownloadMonitor.context.dataset.currentVideoUrl;console.log(_m3u8);return _m3u8;}return m3u8print();")
    print(videoUrl)
    browser.get("https://www.baidu.com")
    return videoUrl