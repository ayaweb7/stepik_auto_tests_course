import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля: имя, фамилия, email
    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    input3.send_keys("email@email.com")
    
    # получаем путь к директории текущего исполняемого скрипта lesson2_2_step8.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "file_example.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # находим и выбираем кнопку для отправки файла
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    # отправляем файл
    element.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    print("Тест успешно завершен. 20 сек на закрытие браузера...")
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')


finally:
    alert=browser.switch_to_alert() # скрапим всплывающее сообщение
    print('---------------------------------\n\n\n\n',alert.text)# выводим его в консоль
    # ожидание чтобы визуально оценить результаты прохождения скрипта - успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson2_2_step8.py