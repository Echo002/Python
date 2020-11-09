from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('B站')
driver.find_element_by_id('su').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()