import random
import re

from model.contact import Contact
from model.group import Group


def test_del_contact_from_group(app, db):
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    new_groups = db.get_group_list()
    group = random.choice(new_groups)
    old_contacts = db.get_contact_list()
    num = group.id
    index = random.randrange(len(old_contacts))
    if len(db.get_contacts_in_group(num)) == 0:
        app.contact.add_contact_to_group(index, group.name)
    old_contacts_in_group = sorted(app.contact.get_contacts_in_group(group_name=group.name), key=Contact.id_or_max)
    contacts_num = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group(group.name, contacts_num.id)
    old_contacts_in_group.remove(contacts_num)
    new_contacts_in_group = db.get_contacts_in_group(num)
    for i in range(len(old_contacts_in_group)):
        assert old_contacts_in_group[i].id == clear(new_contacts_in_group[i].id)


def clear(s):
    return re.sub("[() ,]", "", s)
