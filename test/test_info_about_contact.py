import re
from model.contact import Contact


def test_check_contact_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    list = {}
    for contact in contact_from_home_page:
        list.setdefault(contact.id, contact)
    for contact in contact_from_db:
        contact_from_home_page = list[contact.id]
        assert contact_from_home_page.lastname == contact.lastname.rstrip()
        assert contact_from_home_page.firstname == contact.firstname
        assert clear(contact_from_home_page.address) == clear(contact.address)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact)


def clear(s):
    return re.sub("[() -]", "", str(s))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
