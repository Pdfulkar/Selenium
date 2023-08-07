from selenium.webdriver.common.by import By


class loginPage:

    def __init__(self,driver):

        self.driver = driver
        self.usename_textbox = (By.ID, "student")
        self.password_textbox = (By.ID, "Password123")
        self.login_button = (By.ID,"submit" )

    def open_page(self,url):
        self.driver.get(url)

    def enter_username(self,username):
        self.driver.find_element(self.usename_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(self.login_button).click()