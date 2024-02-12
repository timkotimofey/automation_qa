from datetime import datetime

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():  # This function which creates driver
    # SET UP of fixture (before running our test)
    driver = webdriver.Chrome()  # With help this command I run our browser
    driver.maximize_window()  # Open window full screen

    # TEAR DOWN of fixture (after running our test)
    yield driver  # yield  it is like return. After return cant write the code, but after yield i can
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
