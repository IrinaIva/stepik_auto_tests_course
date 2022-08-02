from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-features=RendererCodeIntegrity")
browser = webdriver.Chrome(chrome_options=chrome_options)

try:
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input3 = browser.find_element(by=By.XPATH, value="/html/body/div/form/div[1]/div[1]/input")
    input3.send_keys("First name")
    input4 = browser.find_element(by=By.XPATH, value="/html/body/div/form/div[1]/div[2]/input")
    input4.send_keys("Last name")
    input5 = browser.find_element(by=By.XPATH, value="/html/body/div/form/div[1]/div[3]/input")
    input5.send_keys("Email")



    input1 = browser.find_element(By.CSS_SELECTOR, "//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input2.send_keys("Popov")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input3.send_keys("test33@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



# не забываем оставить пустую строку в конце файла

