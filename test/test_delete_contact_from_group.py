import random
from model.group import Group
from model.contact import Contact


def test_delete_contact_from_group(app, orm, db, check_ui):
    if len(orm.get_groups_list()) == 0:
        initial_group = Group(name="test_group")
        app.group.create(initial_group)
    if len(orm.get_contacts_list()) == 0:
        initial_contact = Contact(firstname="test")
        app.contact.create(initial_contact)
        app.contac.add_contact_in_group(initial_contact.id, initial_group.id)
    groups = orm.get_groups_list()
    selected_group = random.choice(groups)
    contacts_in_selected_group = orm.get_contacts_in_group(selected_group)
    if len(contacts_in_selected_group) == 0:
        selected_contact = random.choice(orm.get_contacts_list())
        app.contact.add_contact_in_group(selected_contact.id, selected_group.id)
        contacts_in_selected_group = orm.get_contacts_in_group(selected_group)
    selected_contact = random.choice(contacts_in_selected_group)
    app.contact.delete_contact_from_group(selected_contact.id, selected_group.id)
    contacts_in_group = orm.get_contacts_in_group(selected_group)
    assert selected_contact not in contacts_in_group

