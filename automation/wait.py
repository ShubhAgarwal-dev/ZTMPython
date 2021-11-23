from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

ser = Service(r'.\automation\geckodriver.exe')
opts = Options()
opts.add_argument("--headless")

firefox_instance = webdriver.Firefox(options=opts, service=ser)

firefox_instance.get(
    "https://demo.seleniumeasy.com/basic-first-form-demo.html")


assert 'Selenium Easy Demo' in firefox_instance.title

button_element = firefox_instance.find_element_by_class_name("btn-default")

assert 'Show Message' in firefox_instance.page_source

user_message = firefox_instance.find_element_by_id("user-message")
user_message.clear()
message = "Hello we can make python do it."
user_message.send_keys(message)
firefox_instance.implicitly_wait(3)
button_element.click()
output_message = firefox_instance.find_element_by_id("display")

assert message in output_message.get_attribute('innerHTML')

firefox_instance.close()
