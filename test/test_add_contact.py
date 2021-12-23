# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="",
                    homepage="", byear="", ayear="", address2="", phone2="", notes="")]+[
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
            nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 20),
            address=random_string("address", 10), home_phone=random_string("home_phone", 20), mobile_phone=random_string("mobile_phone", 20),
            work_phone=random_string("work_phone", 10), fax=random_string("fax", 20), email=random_string("email", 20),
            email2=random_string("email2", 10), email3=random_string("email3", 20), homepage=random_string("homepage", 20),
            byear=random_string("byear", 10), ayear=random_string("ayear", 20), address2=random_string("address2", 20),
            phone2=random_string("phone2", 20), notes=random_string("notes", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
