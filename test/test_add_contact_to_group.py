from model.contact import Contact
from model.group import Group
import random
import re


def test_add_some_contact_to_group(app, db):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    new_groups = db.get_group_list()
    group = random.choice(new_groups)
    num = group.id
    old_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_in_group = db.get_contacts_in_group(num)
    list = app.contact.check_all_contacts_in_group(old_contacts, contacts_in_group)
    if not list:
        app.contact.create(Contact(firstname="test"))
        new_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
        list.append(new_contacts[-1].id)
    id = random.choice(list)
    app.contact.add_contact_to_group(id, group.name)
    contact_from_ui = sorted(app.contact.get_contacts_in_group(group_name=group.name), key=Contact.id_or_max)
    contact_from_db = db.get_contacts_in_group(num)
    for i in range(len(contact_from_ui)):
        assert contact_from_ui[i].id == clear(contact_from_db[i].id)


def clear(s):
    return re.sub("[() ,]", "", s)
