from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage

### POM : Page object model ### interview question.. Have you worked with POM?
class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    __name = (By.CSS_SELECTOR, "[name='name']")     ## private attribute
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):      ## getter # readonly method for __name attribute
        return self.driver.find_element(*HomePage.__name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)    # * is used to unpack tuple in parameters
        ## HomePage.email[0], HomePage.email[1] => *HomePage.email


    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)




