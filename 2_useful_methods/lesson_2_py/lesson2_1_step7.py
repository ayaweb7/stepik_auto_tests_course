from selenium import webdriver
import time
import math

# Функция для вычисления значений
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открывает страницу сайта в новом браузере
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    valuex = browser.find_element_by_id("treasure")    # находит элемент, содержащий переменную
    chest = valuex.get_attribute("valuex")             # присваивает переменной её значение
    print('Значение переменной = ', chest)             # печатает значение переменной
    y = calc(chest)                                    # вычисляет функцию с переменной

# находит поле для ввода ответа и вводит ответ в поле формы    
    browser.find_element_by_id('answer').send_keys(y)
    
# найти и кликнуть radiobutton    
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    
# найти и кликнуть по чекбоксу    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
# найти и кликнуть кнопку отправки формы
    browser.find_element_by_class_name("btn.btn-default").click()
    time.sleep(5)
    
finally:
    alert=browser.switch_to_alert() # скрапим всплывающее сообщение
    print('---------------------------------\n\n\n\n',alert.text)# выводим его в консоль
    # ожидание чтобы визуально оценить результаты прохождения скрипта - успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
#    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson2_1_step7.py