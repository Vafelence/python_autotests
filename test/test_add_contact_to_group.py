from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm, db):
    if len(db.get_groups_without_contacts()) == 0:
        app.group.create(Group(name="test_group"))

    if len(db.get_contacts_not_in_any_group()) == 0:
        app.contact.create(Contact(firstname="test"))

    groups = db.get_groups_without_entries()
    selected_group = random.choice(groups)

    contacts = db.get_contact_not_in_any_group()
    selected_contact = random.choice(contacts)

    app.contact.add_contact_in_group(selected_contact.id, selected_group.id)

    contacts_in_group = orm.get_contacts_in_group(selected_group)

    assert selected_contact in contacts_in_group


def test_delete_entry_from_group(app, orm, db, check_ui):
    if len(orm.get_group_list()) == 0:
        initial_group = Group(name="test_group")
        app.group.create(initial_group)

    if len(orm.get_contact_list()) == 0:
        initial_contact = Contact(firstname="test")
        app.contact.create(initial_contact)
        app.contact.add_contact_in_group(initial_contact.id, initial_group.id)

    groups = orm.get_group_list()
    selected_group = random.choice(groups)

    contacts_in_selected_group = orm.get_contacts_in_group(selected_group)

    if len(contacts_in_selected_group) == 0:
        selected_contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_in_group(selected_contact.id, selected_group.id)
        contacts_in_selected_group = orm.get_contacts_in_group(selected_group)

    selected_contact = random.choice(contacts_in_selected_group)

    app.contact.delete_contact_from_group(selected_contact.id, selected_group.id)

    contacts_in_group = orm.get_contacts_in_group(selected_group)

    assert selected_contact not in contacts_in_group