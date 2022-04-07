from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"
link_login = "https://stepik.org/"
link_answer = "https://stepik.org/lesson/138920/step/4?unit=196194"

try:
    # get verification code
    browser = webdriver.Firefox()
    browser.get(link)

    first_name = "first_name"
    last_name = "last_name"
    city = "city"
    country = "country"

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys(first_name)
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys(last_name)
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys(city)
    input4 = browser.find_element_by_id("country")
    input4.send_keys(country)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    text_alert = alert.text
    answer_value = text_alert[(text_alert.index(': '))+2:]
    time.sleep(5)
    alert.accept()

    # log in
    browser.get(link_login)
    time.sleep(5)

    submit_button = browser.find_element_by_css_selector(".navbar__auth")
    submit_button.click()

    login_email = "e-mail"
    login_password = "password"

    s_username = browser.find_element_by_id("id_login_email")
    s_username.send_keys(login_email)

    s_password = browser.find_element_by_id("id_login_password")
    s_password.send_keys(login_password)

    button = browser.find_element_by_css_selector(".sign-form__btn")
    button.click()

    time.sleep(5)

    # input verification code in textarea
    browser.get(link_answer)
    time.sleep(5)

    textarea = browser.find_element_by_css_selector(".textarea")
    textarea.send_keys(answer_value)
    time.sleep(5)

    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    time.sleep(5)

finally:
    time.sleep(30)
    # close browser
    browser.quit()

# не забываем оставить пустую строку в конце файла
    
# не забываем оставить пустую строку в конце файла
# python lesson6_step4_1.py