import re
from model.contact import Contact


def test_info_on_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(contact = Contact(firstname="Roman", middlename="Sergeevich", lastname="Yatskin", nickname="tester",
                       title="123", company="X5", address="Moscow", home_phone="+79999999999", mobile_phone="+78888888888",
                       work_phone="+77777777777", fax="+76666666666", email="1@1.ru", email2="2@2.ru",
                       email3="3@4.ru", homepage="google.com", bday="6", bmonth="June", byear="1990",
                       aday="5", amonth="May", ayear="1991", address2="Moscow City", phone2="+75555555555",
                       notes="tester123"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,[contact.home_phone, contact.mobile_phone,
                                                                contact.work_phone, contact.phone2]))))
