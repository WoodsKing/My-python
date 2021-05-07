# class定位类前加. class = 'serch' driver.find_element_by_css_selector('.serch')
# id定位前加#   id = 'wd' driver.find_element_by_css_selector('#id')
# type定位直接写    <input>标签  driver.find_element_by_css_selector('input')
from selenium import webdriver
from selenium.webdriver.common.by import By

brower = webdriver.Chrome()
brower.get('https://www.taobao.com/')


input_id = brower.find_element_by_id('J_TSearchForm')
input_name = brower.find_element_by_name('search')
print(input_name)
print(input_id)

# find_element(By.ID,id)查找方式  等价与find_element_by_id(id)
input_ele = brower.find_element(By.ID, 'J_TSearchForm')
print(input_ele)

# 查找多个节点
input_class = brower.find_elements_by_css_selector('.J_Cat.a-all')
print('\n\n\n\n', input_class)

brower.close()