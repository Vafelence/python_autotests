# -*- coding: utf-8 -*-
from application import Application
from contact import Contact
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Roman", middlename="Sergeevich", lastname="Yatskin", nickname="tester",
                                            title="123", company="X5", address="Moscow", home="+79999999999", mobile="+78888888888",
                                            work="+77777777777", fax="+76666666666", email="1@1.ru", email2="2@2.ru",
                                            email3="3@4.ru", homepage="google.com", bday="2", bmonth="June", byear="1990",
                                            aday="5", amonth="May", ayear="1991", address2="Moscow City", phone2="+75555555555",
                                            notes="tester123"))
    app.logout()
