from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm, db):
    if len(db.get_groups_without_contacts()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contacts_not_in_any_group()) == 0:
        app.contact.create(Contact(firstname="test"))
    groups = db.get_groups_without_contacts()
    selected_group = random.choice(groups)
    contacts = db.get_contacts_not_in_any_group()
    selected_contact = random.choice(contacts)
    app.contact.add_contact_in_group(selected_contact.id, selected_group.id)
    contacts_in_group = orm.get_contacts_in_group(selected_group)
    assert selected_contact in contacts_in_group
