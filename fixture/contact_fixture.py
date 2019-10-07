import time

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_form_value("firstname", contact.firstname)
        self.change_contact_form_value("lastname", contact.lastname)
        self.change_contact_form_value("mobile", contact.mobile)

    def change_contact_form_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.contact_fixture.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        time.sleep(2)

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        if len(wd.find_element_by_name("selected[]")) > 0:
            wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_element_by_xpath("input[@type='checkbox' and @name='selected[]']"))




