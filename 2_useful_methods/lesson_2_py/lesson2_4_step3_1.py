from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(2)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    static_message = "Verification was successful!"
   
    assert static_message == message.text, "Сообщение в алерте не то, что надо"
    
finally:
    time.sleep(2)
    browser.quit()

# не забываем оставить пустую строку в конце файла
# python lesson2_4_step3_1.py