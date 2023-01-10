from utilities.BaseClass import BaseClass
import pytest

class Test_CheckOutPageByMe(BaseClass):

    def test_operarionCheckOut(self):
        CheckoutPage(self.driver)