from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

ser = Service(r'.\automation\geckodriver.exe')
opts = Options()
opts.add_argument("--headless")
# if running in headless mode please remember to close background firefox running

firefox_instance = webdriver.Firefox(options=opts, service=ser)

# firefox_instance.maximize_window()
# -> Actually it is not required as firefox runs by default in maximize window mode but others do not and totally useless of ypu are running browser headless
firefox_instance.get(
    "https://demo.seleniumeasy.com/basic-first-form-demo.html")


assert 'Selenium Easy Demo' in firefox_instance.title
# We can also use print and it will not error out

button_element = firefox_instance.find_element_by_class_name("btn-default")
# we can also use find_element_by_css_selector("#get-input > .btn") Note: # tells that it is ID and . tells us that is css class
# print(button_element.get_attribute('innerHTML'))

assert 'Show Message' in firefox_instance.page_source

user_message = firefox_instance.find_element_by_id("user-message")
user_message.clear()
message = "Hello we can make python do it."
user_message.send_keys(message)
button_element.click()
output_message = firefox_instance.find_element_by_id("display")

assert message in output_message.get_attribute('innerHTML')

firefox_instance.close()
firefox_instance.close()
# Sometimes you are required to close it twice because it might not work for first time for some weird bugs
# firefox_instance.quit() would close all the instanced opened in the window but some bug can happen
firefox_instance.quit()
'''
we can add delay between our actions to make them look more human like so that our test might fail because of nit detection
'''
