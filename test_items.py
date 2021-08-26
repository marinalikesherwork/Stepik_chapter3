import pytest
import time
from selenium import webdriver
	
class TestButtonAddToCart:
    def test_find_button(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
        assert button > 0, "Button not found"