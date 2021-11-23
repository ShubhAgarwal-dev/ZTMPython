from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

ser = Service(r'.\automation\geckodriver.exe')
opts = Options()
opts.add_argument("--headless")
# if running in headless mode please remember to close background firefox running

firefox_instance = webdriver.Firefox(options=opts, service=ser)

firefox_instance.maximize_window()
# -> Actually it is not required as firefox runs by default in maximize window mode but others do not
firefox_instance.get(
    "https://demo.seleniumeasy.com/basic-first-form-demo.html")


assert 'Selenium Easy Demo' in firefox_instance.title
# We can also use print and it will not error out

button_element = firefox_instance.find_element_by_class_name("btn-default")
print(button_element.get_attribute('innerHTML'))

assert 'Show Message' in firefox_instance.page_source

user_message = firefox_instance.find_element_by_id("user-message")
user_message.clear()
message = "Hello we can do it."
user_message.send_keys(message)
