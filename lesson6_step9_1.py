from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    labels = browser.find_elements_by_tag_name('label') # Список лэйблов над текстовыми полями
    inputs = browser.find_elements_by_tag_name('input') # Список текстовых полей

    for i, label in enumerate(labels):          # Если последний символ
        if label.text[-1] == '*':               # лейбла над текстовым полем равен "*",
            inputs[i].send_keys('Обязалово!')   # то в поле ввода печатаем "Обязалово!"

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = browser.find_element_by_tag_name("h1").text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson6_step9_1.py