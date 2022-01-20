from model.contact import Contact
import random
import allure


def test_modify_contact(app, db, json_contact, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    with allure.step("Given an contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("Given a selected contact"):
        contact = json_contact
        select_contact = random.choice(old_contacts)
        contact.id = select_contact.id
    with allure.step("When I edit the contact"):
        app.contact.modify_contact_by_id(select_contact.id, contact)
    with allure.step("Then the contact list is equal to the old list with the edited contact"):
        new_contacts = db.get_contact_list()
        old_contacts.remove(select_contact)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)