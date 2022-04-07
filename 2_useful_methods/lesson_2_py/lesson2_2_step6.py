from selenium import webdriver
import time
import math

# Считает формулу на странице
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#Открывает браузер
try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")   #находит переменную
    x = x_element.text                                      #присваивает ее за х
    y = calc(x)                                             #высчитывает формулу с х
    print('f(', x, ') = ', y)

    #находит поле для ввода ответа
    input1 = browser.find_element_by_xpath('//input[@type="text"]') 
    input1.send_keys(y)
    
    # Скроллим документ вниз до тех пор, пока не будет видна кнопка отправки формы
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    #найти и кликнуть по чекбоксу
    option1 = browser.find_element_by_xpath('//input[@type="checkbox"]')
    option1.click()

    #найти и кликнуть radiobutton
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

#    button = browser.find_element_by_xpath('//button[@type="submit"]')
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
# python lesson2_2_step6.py