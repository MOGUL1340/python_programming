# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_group(app):
    app.group_fixture.create_group(Group(name="", header="", footer=""))

def test_add_group(app):
    app.group_fixture.create_group(Group(name="adsfger", header="ahdhgftr", footer="agdgfdrer"))





