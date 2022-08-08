import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

def test_see_add_button(browser):
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//form[@id='add_to_basket_form']//button")))



