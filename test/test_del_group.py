from model.group import Group

def test_delete_first_group(app):
    if app.group_fixture.count == 0:
        app.group_fixture.create_group(Group(name="test"))
    app.group_fixture.delete_first_group()
