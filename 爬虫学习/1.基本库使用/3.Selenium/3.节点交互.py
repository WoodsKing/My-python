from selenium import webdriver
import time

brower = webdriver.Chrome()
brower.get('https://www.taobao.com')
input = brower.find_element_by_id('q')
input.send_keys('拖鞋')
time.sleep(1)
button = brower.find_element_by_css_selector('.btn-search.tb-bg')
button.click()