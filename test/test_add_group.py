# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_group(app):
    old_groups = app.group_fixture.get_group_list()
    app.group_fixture.create_group(Group(name="", header="", footer=""))
    new_groups = app.group_fixture.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_group(app):
    old_groups = app.group_fixture.get_group_list()
    app.group_fixture.create_group(Group(name="adsfger", header="ahdhgftr", footer="agdgfdrer"))
    new_groups = app.group_fixture.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)





