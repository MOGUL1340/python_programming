# -*- coding: utf-8 -*-
from model.contact import Contact

def test_new_contact(app):
    # app.open_home_page()
    # app.session.login(username="admin", password="secret")
    app.contact_fixture.new_contact(Contact(firstname="Adi", lastname="Das", mobile="+30480001234"))
    # app.return_homepage()
    # app.session.logout()









