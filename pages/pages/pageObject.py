class Home:
    def __init__(self,driver):
        self.URL="https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        self.driver=driver
        self.email='henriquemargarido3@gmail.com'
        self.passw='03Zucacida'
        self.elementEmail='//*[@id="identifierId"]'
        self.elementPass='//*[@id="password"]/div[1]/div/div[1]/input'
        self.enterEmail='//*[@id="identifierNext"]/content/span'
        self.enterPass='//*[@id="passwordNext"]/content/span'

        self.compose='//*[@id=":jy"]/div/div'

        self.enterTo=":py"
        self.enterTitle=":pg"
        self.enterBodyText=":ql"

        self.to="henrique_margarido@hotmail.com"
        self.title="teste100"
        self.bodyText="epiwjfwiejjifejwoi"
        self.buttonEmail='//*[@id=":p6"]'

    def go_home(self):
        self.driver.get(self.URL)

    def put_data(self):
        self.driver.find_element_by_xpath(self.elementEmail).send_keys(self.email)
        
        self.driver.find_element_by_xpath(self.enterEmail).click()

        self.driver.implicitly_wait(1)

        self.driver.find_element_by_xpath(self.elementPass).send_keys(self.passw)

        self.driver.find_element_by_xpath(self.enterPass).click()

        self.driver.implicitly_wait(1)
    
    def open_compose(self):
        self.driver.find_element_by_xpath(self.compose).click()

    def bodyEmail(self):
        self.driver.implicitly_wait(2)

        self.driver.find_element_by_id(self.enterTo).send_keys(self.to)

        self.driver.find_element_by_id(self.enterTitle).send_keys(self.title)

        self.driver.find_element_by_id(self.enterBodyText).send_keys(self.bodyEmail)

    def sendEmail(self):
        self.driver.find_element_by_xpath(self.buttonEmail).click()