from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link = "http://suninjuly.github.io/find_link_text"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-features=RendererCodeIntegrity")
browser = webdriver.Chrome(chrome_options=chrome_options)
link2 = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser.get(link)
    button = browser.find_element(By.LINK_TEXT, link2)
    button.click()
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "firstname")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла