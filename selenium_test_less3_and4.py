from selenium import webdriver
driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
driver.implicitly_wait(5)
# driver.get('https://translate.google.co.il')
driver.get('https://gofile.io/?t=uploadFiles')

print(driver.current_url)
print(driver.title)
#print(driver.page_source)
#driver.quit()
# my_find = driver.find_element_by_id("source").send_keys("hello")
# my_find = driver.find_element_by_id("source").send_keys(Keys.ENTER)
# my_find = driver.find_element_by_id("source").click()
# my_find2 = driver.find_element_by_xpath('//*[@rows="1"]')
#print(len(my_find))
#print(len(my_find2))

# elements = driver.find_elements_by_id("source").click()
# #lements[0].click()
# print(len(elements))

#
# source_element = driver.find_element_by_id("source")
# if source_element.is_enabled():
#     source_element.click()
#
# print("value", source_element.get_attribute("rows"))


source_element = driver.find_element_by_id("source")
