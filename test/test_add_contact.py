from model.contact import Contact


def test_add_contact(app, db, json_contact, check_ui):
    contact = json_contact
    old_contacts = db.get_contact_list()
    contact_id = app.contact.create(contact)
    contact.id = contact_id
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.entry.get_entries_list(), key=Contact.id_or_max)
