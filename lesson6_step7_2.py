from selenium import webdriver
import time
import random
import string

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver\chromedriver.exe')
# подавление ошибки юсб ERROR:device_event_log_impl.cc(214)
#  USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection:
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))

# заполняем поле  случайными 8 буквами
    time.sleep(3)
    button = browser.find_element_by_xpath('//button')
    button.click()

finally:
    alert=browser.switch_to_alert() # скрапим всплывающее сообщение
    print('---------------------------------\n\n\n\n',alert.text)# выводим его в консоль
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson6_step7_2.py