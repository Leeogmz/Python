from selenium import webdriver

class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'APjFqb'  # id
        self.btn_search = 'btnK'  # name
        self.btn_lucky = 'btnI'  # name

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='None'):
        self.driver.find_element_by_id(
            self.search_bar).send_keys(word)
        self.driver.find_element_by_name(
            self.btn_search).click()

    def lucky(self, word='None'):
        self.driver.find_element_by_id(
            self.search_bar).send_keys(word)
        self.driver.find_element_by_name(
            self.btn_lucky).click()


ff = webdriver.Chrome()
g = Google(ff)
g.navigate()