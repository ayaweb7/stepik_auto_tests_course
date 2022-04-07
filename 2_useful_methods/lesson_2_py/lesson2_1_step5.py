from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
#    x_element = browser.find_element_by_*(selector)
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    browser.find_element_by_class_name("btn.btn-default").click()
    time.sleep(5)
    
finally:
    alert=browser.switch_to_alert() # скрапим всплывающее сообщение
    print('---------------------------------\n\n\n\n',alert.text)# выводим его в консоль
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson2_1_step5.py