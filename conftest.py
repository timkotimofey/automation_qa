import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():                                                   # this function which creates driver
    # SET UP of fixture (before running our test)
    driver = webdriver.Chrome(ChromeDriverManager().install())  # with help this command we run our browser
    driver.maximize_window()                                    # open window full screen

    # TEAR DOWN of fixture (after running our test)
    yield driver                                                # yield  it is like return. After return cant write the code, but after yield i can
    driver.quit()