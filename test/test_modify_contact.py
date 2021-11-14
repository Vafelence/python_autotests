from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="Roma", middlename="Sergeevi4", lastname="Unknown", nickname="Test Engineer",
                       title="Love Job", company="X5Tech", address="Russia", home="+75555555555", mobile="+74444444444",
                       work="+73333333333", fax="+72222222222", email="4@4.ru", email2="5@5.ru",
                       email3="6@6.ru", homepage="yandex.com", bday="3", bmonth="October", byear="1891",
                       aday="9", amonth="January", ayear="1901", address2="Vladivostok", phone2="+71111111111",
                       notes="try to automate, mate"))
    app.session.logout()
