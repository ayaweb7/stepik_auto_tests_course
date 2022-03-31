from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

# Считает формулу на странице
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Загружаем браузер, открываем страницу https://...
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # говорим Selenium проверять в течение 12 секунд, пока цена не станет = $100
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Находим кнопку "Book" и жмём на неё.
    button_book = browser.find_element_by_id("book")
    button_book.click()

    # Скроллим документ вниз до тех пор, пока не будет видна кнопка отправки формы
    button_submit = browser.find_element_by_xpath('//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    
    x_element = browser.find_element_by_id("input_value")   #находит переменную
    x = x_element.text                                      #присваивает ее за х
    y = calc(x)                                             #высчитывает формулу с х
    print('f(', x, ') = ', y)

    #находит поле для ввода ответа
    input_result = browser.find_element_by_xpath('//input[@type="text"]') 
    input_result.send_keys(y)
    
    #Нажать на кнопку "Отправить".
    button_submit.click()
    
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
# python lesson2_4_step8.py