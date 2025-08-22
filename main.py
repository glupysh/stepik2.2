import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

url = 'https://suninjuly.github.io/file_input.html'
data_list = ['Vlad', 'Petrov', 'vld_ptr@mail.ru', file_path]
field_names = ['firstname', 'lastname', 'email', 'file']

with webdriver.Chrome() as browser:
    browser.get(url)
    for index in range(4):
        browser.find_element(By.NAME,field_names[index]).send_keys(data_list[index])

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    alert = browser.switch_to.alert.text
    print(alert)