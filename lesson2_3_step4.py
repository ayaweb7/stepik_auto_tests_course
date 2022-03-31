from selenium import webdriver
import time
import math

# Считаем математическую функцию от x.
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Загружаем браузер, открываем страницу https://... 
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим кнопку "Отправить" и жмём на неё.
    browser.find_element_by_class_name("btn.btn-primary").click()

    # Переключаемся на окно confirm и принимаем alert
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # Находим поле со значением для вычисления функции, считаем значение для переменной x,
    # находим поле для ввода ответа и вводим ответ
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    
    # Находим кнопку "Отправить" и жмём на неё.
    browser.find_element_by_class_name("btn.btn-primary").click()

    print("Тест успешно завершен. 20 сек на закрытие браузера...")
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

    
finally:
    alert=browser.switch_to_alert() # скрапим всплывающее сообщение
    print('---------------------------------\n\n\n\n',alert.text)# выводим его в консоль
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson2_3_step4.py