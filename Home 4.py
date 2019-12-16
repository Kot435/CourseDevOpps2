#1

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# driver.get('http://www.walla.co.il')

#2
# In one of the browsers you open do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you
# created in clause 1.

# title = driver.title
# print(title)
# driver.refresh()
# if title==driver.title:
#     print("from diver title:", driver.title)

#3
# Open a few browsers, locate any element, does the
# element has the same locators in the other browser?
#???

#4
# Create a test with the following:
# Open Google Translate web page
# Write anything in Hebrew in the text area

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# driver.get('https://translate.google.com')
# driver.find_element_by_id("source").send_keys("שלום")


#5
# Open Youtube web page
# Type a name of a song
# Click on search.

# from selenium import webdriver
# # driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# # driver.get('https://www.youtube.com/')
# # driver.find_element_by_id("search").send_keys("pop music 2019 clean")
# # driver.find_element_by_id("search-icon-legacy").click()

#6
# Find translation text field (the one you send keys to)
# with 3 different locators and print the WebElement you created
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# driver.get('https://translate.google.com')
# elmt = driver.find_element_by_id("source")
# elmt2 = driver.find_element_by_class_name("orig")
# elmt3 = driver.find_element_by_xpath('//*[@rows="1"]')
# print("elmt",elmt)
# print("elmt2",elmt2)
# print("elmt3",elmt3)

#7
# Open Chrome browser on Facebook website
# Login into Facebook
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# driver.get('https://www.facebook.com')
# driver.find_element_by_id("email").send_keys("tolkantoren@eopleopp.shop")
# driver.find_element_by_id("pass").send_keys("tolkantoren")

#8
# Open Chrome browser on any webpage.
# Delete all cookies from browser.
# Make sure all cookies are deleted by printing all cookies stored in the browser.
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# driver.get('http://www.walla.co.il')
# my_delete = driver.delete_all_cookies()
# print("my_delete", my_delete)

#9
# Open any browser on "Github" website.
# https://github.com/
# Enter “Selenium” keyword in search textfield
# Press Enter to search (through code - of course)
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# driver.get('https://github.com/')
# #driver.find_element_by_id("text").send_keys("Selenium")
# driver.find_element_by_xpath('//*[@role="search"]').click()
# driver.find_element_by_name("q").send_keys("Selenium")
# driver.find_element_by_name("q").submit()

#10
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='F:\\DevOpps\selenium\chromedriver.exe')
# driver.get('https://github.com/')

#????




