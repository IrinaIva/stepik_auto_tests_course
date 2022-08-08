from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
options = webdriver.ChromeOptions()
options.add_argument("-disable-features=RendererCodeIntegrity")
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(5)

try:
    browser.get(link)
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)


    #x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input3 = browser.find_element(By.ID, "answer")
    input3.send_keys(y)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

# не забываем оставить пустую строку в конце файла

