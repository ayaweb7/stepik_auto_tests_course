from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
#    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

# Определение 1-го и 2-го слагаемых и их суммы
    num_1 = browser.find_element_by_id("num1").text
    num_2 = browser.find_element_by_id("num2").text
    s = str(int(num_1) + int(num_2))
    print('link = ', link)
    print(num_1, ' + ', num_2, ' = ', s)

# Выбор из списка значения, соответствующего сумме слагаемых    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(s)

# Отправка результата
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    
    print("Тест успешно завершен. 20 сек на закрытие браузера...")

finally:
    alert=browser.switch_to_alert() # скрапим всплывающее сообщение
    print('---------------------------------\n\n\n\n',alert.text)# выводим его в консоль
    # ожидание чтобы визуально оценить результаты прохождения скрипта - успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла
# python lesson2_2_step3.py