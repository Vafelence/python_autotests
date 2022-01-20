import random
from model.group import Group
from model.contact import Contact


def test_remove_contact_from_group(app, orm):
    if len(orm.get_groups_list()) == 0:
        app.group.create(Group(name='test'))
    group = random.choice(orm.get_groups_list())
    if len(orm.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname='test'))
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(orm.get_contacts_not_in_group(group))
        app.contact.add_contact_in_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_contact_from_group(contact, group)
    assert contact not in orm.get_contacts_in_group(group)
