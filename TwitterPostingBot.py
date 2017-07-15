import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import selenium.webdriver.support.ui as ui



# logging into twitter
# You must download the geckodriver for firefox
# or whichever drive you want to use for whichever browser you prefer...
driver = webdriver.Firefox(executable_path=r'put the file path to geckodriver here like this: /Users/.../geckodriver')
driver.get("https://twitter.com/login")

# User name and password
username = driver.find_element_by_class_name("js-username-field")
username.send_keys("put_your_username_here")

#browser must pause so that the elements will load
time.sleep(10)
password = driver.find_element_by_class_name("js-password-field")
password.send_keys("put_your_password_here")


wait = ui.WebDriverWait(driver, 5)
#submit to login 
driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()

#Sharing articles from your website
#bot goes to your website
driver.get("your_website_here.com")
time.sleep(5)

#Sharing n amount of articles
# copy and paste this codeblock, just change the link...
driver.get("put your sharing article link here: >right click on the twitter>open in new tab > copy the url > paste it here to replace this text ")
time.sleep(5)
addHash = driver.find_element_by_xpath('//*[@id="status"]')
addHash.send_keys("#ADD #YOUR #Hashtags here ")
time.sleep(7)
driver.find_element_by_xpath('//*[@id="update-form"]/div[3]/fieldset/input[2]').click()
# closes the browser 
driver.quit()
