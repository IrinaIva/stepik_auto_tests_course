import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


options = webdriver.ChromeOptions()
options.add_argument("-disable-features=RendererCodeIntegrity")
url = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
]
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', url)
def test_guest_should_see_login_link(browser, url):
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[id^="ember"]')))
    answer = math.log(int(time.time()))
    inputf = browser.find_element(By.CSS_SELECTOR, 'textarea[id^="ember"]')
    inputf.send_keys(answer)
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p[class="smart-hints__hint"]')))
    result_text = browser.find_element(By.CSS_SELECTOR, 'p[class="smart-hints__hint"]')
    result_text = result_text.text
    assert "Correct!" == result_text
