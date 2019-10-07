# -*- coding: utf-8 -*-
from model.contact import Contact

def test_new_contact(app):
    app.contact_fixture.add_new_contact(Contact(firstname="Adi", lastname="Das", mobile="+30480001234"))










