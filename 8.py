from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-features=RendererCodeIntegrity")
browser = webdriver.Chrome(chrome_options=chrome_options)

try:
    #browser.get(link)
    # Ваш код, который заполняет обязательные поля
    browser.execute_script("alert('Robots at work');")

    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_visible_text(str(summ))  # ищем элемент с текстом "Python"


    # Отправляем заполненную форму
    #button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    #button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



# не забываем оставить пустую строку в конце файла

