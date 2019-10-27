# -*- coding: utf-8 -*-
from model.contact import Contact

def test_new_contact(app):
    old_contacts = app.contact.add_contact_list()
    contact = Contact(firstname="Adi", lastname="Das", nickname="Adidas", company="test", email="adi@das.com", bday="18", bmonth="August", byear="1949")
    app.contact.create(contact)
    new_contacts = app.contact.add_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)










