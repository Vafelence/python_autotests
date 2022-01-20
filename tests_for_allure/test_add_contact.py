from model.contact import Contact
import allure


def test_add_contact(app, db, json_contact, check_ui):
    contact = json_contact
    with allure.step("Given an contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("When I add the contact to the list"):
        contact_id = app.contact.create(contact)
    with allure.step("Then the new contact list is equal to the old list with the added contact"):
        contact.id = contact_id
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.entry.get_entries_list(), key=Contact.id_or_max)
