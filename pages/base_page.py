

class BasePage:            # This is parent (basic) class. Other classes were inherit from this class
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)