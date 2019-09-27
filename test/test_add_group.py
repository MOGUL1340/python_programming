# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group_fixture.create_group(Group(name="", header="", footer=""))
    app.session.logout()


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group_fixture.create_group(Group(name="adsfger", header="ahdhgftr", footer="agdgfdrer"))
    app.session.logout()




