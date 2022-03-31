from selenium import webdriver
import time
import random

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Krasavino', 'Koryazha']

from selenium import webdriver
from random import choice
import string

def GenRandomLine(length=5, chars=string.ascii_lowercase + string.digits):
    return ''.join([choice(chars) for i in range(length)])

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    [element.send_keys(GenRandomLine()) for element in browser.find_elements_by_css_selector("[required]")]
    browser.find_element_by_css_selector("button.btn").click()

except Exception as e:
    print(e)

finally:
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson6_step7_1.py