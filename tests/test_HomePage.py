
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


## 1. Starting point
## 2. Before start executing test case it will jump to BaseClass as inheritance
## 3. we will get driver from conftest(setup fixture) via BaseClass
class TestHomePage(BaseClass):      # Inheritance # BaseClass inherited in TestHomePage

    ## First test case to execute on pytest command
    def test_formSubmission(self,getData):
        log = self.getLogger()          #To get logger object from BaseClass
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[{"firstname": "Sagar", "lastname":"Sarade", "Gender": "Male"}, {"firstname": "Yusuf", "lastname":"Tamboli", "Gender": "Male"}])
    ###@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):     #request is default object of fixture which automatically initilized when fixture is being executed
        return request.param


