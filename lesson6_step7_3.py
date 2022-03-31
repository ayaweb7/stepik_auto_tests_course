from selenium import webdriver
import time
import random
import string

link = "http://suninjuly.github.io/huge_form.html"
letters = list(range(97, 123)) + list(range(65, 91))
browser = webdriver.Chrome()
browser.get(link)

try:
    for element in browser.find_elements_by_css_selector("input[type=text]"):
        element.send_keys("".join(map(chr, random.sample(letters, random.randint(2, 14)))))

    button = browser.find_element_by_css_selector("form[method=get] button[type=submit]")
    button.click()

finally:
    alert=browser.switch_to_alert() # скрапим всплывающее сообщение
    print('---------------------------------\n\n\n\n',alert.text)# выводим его в консоль
#    alert.accept()
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson6_step7_3.py