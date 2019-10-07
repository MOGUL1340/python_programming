from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact_fixture.count == 0:
        app.contact_fixture.add_new_contact(Contact(firstname="test", lastname="test", mobile="test"))
    app.contact_fixture.delete_first_contact()