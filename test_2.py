from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)
button = browser.find_element(By.ID, "submit_button")
time.sleep(5)
button.click()
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()