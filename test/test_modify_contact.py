from model.contact import Contact
import random


def test_modify_contact(app, db, json_contact, check_ui):
    if len(db.get_contact_list()) == 0:
        app.entry.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = json_contact
    select_contact = random.choice(old_contacts)
    contact.id = select_contact.id
    app.contact.modify_contact_by_id(select_contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(select_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)