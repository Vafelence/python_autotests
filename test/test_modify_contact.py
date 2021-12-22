from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Roma", middlename="Sergeevi4")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    def test_modify_group_name(app):
        if app.group.count() == 0:
            app.group.create(Group(name="test"))
        old_groups = app.group.get_group_list()
        group = Group(name="update group")
        group.id = old_groups[0].id
        app.group.modify_first_group(group)
        new_groups = app.group.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[0] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)