from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Roma", middlename="Sergeevi4"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
