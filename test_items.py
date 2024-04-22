import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_availability(browser):
    browser.get(link)
    try:
        browser.find_element(By.CLASS_NAME, "btn-primary")
    except NoSuchElementException:
        assert False, "button not found on the page"
