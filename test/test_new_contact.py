# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.new_contact(Contact(firstname="Adi", lastname="Das", mobile="+30480001234"))
    app.return_homepage()
    app.session.logout()








