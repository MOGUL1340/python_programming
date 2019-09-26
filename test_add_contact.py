# -*- coding: utf-8 -*-
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
from contact import Contact
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_create_contact(self):
        wd = self.login()
        self.add_contact(wd, Contact(firstname="Adi", middlename="Dassler", mobile_num="+380480001234"))
        self.return_homepage(wd)
        self.logout(wd)

    def return_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def add_contact(self, contact):
        self.wd.find_element_by_link_text("add new").click()
        self.wd.find_element_by_name("firstname").click()
        self.wd.find_element_by_name("firstname").clear()
        self.wd.find_element_by_name("firstname").send_keys(contact.firstname)
        self.wd.find_element_by_name("middlename").click()
        self.wd.find_element_by_name("middlename").clear()
        self.wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # self.wd.find_element_by_name("lastname").click()
        # self.wd.find_element_by_name("lastname").clear()
        # self.wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # self.wd.find_element_by_name("nickname").click()
        # self.wd.find_element_by_name("nickname").clear()
        # self.wd.find_element_by_name("nickname").send_keys(contact.nickname)
        self.wd.find_element_by_name("mobile").click()
        self.wd.find_element_by_name("mobile").clear()
        self.wd.find_element_by_name("mobile").send_keys(contact.mobile_num)
        # self.wd.find_element_by_name("bday").click()
        # Select(self.wd.find_element_by_name("bday")).select_by_visible_text("1")
        # self.wd.find_element_by_xpath("//option[@value='1']").click()
        # self.wd.find_element_by_name("bmonth").click()
        # Select(self.wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        # self.wd.find_element_by_xpath("//option[@value='January']").click()
        # self.wd.find_element_by_name("byear").click()
        # self.wd.find_element_by_name("byear").clear()
        # self.wd.find_element_by_name("byear").send_keys(contact.byear)
        # self.wd.find_element_by_name("address2").click()
        # self.wd.find_element_by_name("address2").clear()
        # self.wd.find_element_by_name("address2").send_keys(contact.address)
        self.wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self):
        wd = self.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        return wd

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")
        return wd

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
    

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
