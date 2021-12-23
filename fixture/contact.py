import time

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contact_page(self, wd):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # создание нового контакта
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # подтверждение создания нового контакта
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contact_page(wd)
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # выбрать первую группу
        self.select_contact_by_index(index)
        # подтвердить удаление
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def open_contact_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_link_text("All e-mail")) > 0:
            wd.find_element_by_link_text("home").click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # открытие страницы с контактами
        self.open_contact_page()
        self.select_contact_by_index(index)
        # открытие существующего контакта
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # редактирование информации о контакте
        self.fill_contact_form(new_contact_data)
        # подтверждение модификации контакта
        wd.find_element_by_name("update").click()
        self.return_to_contact_page(wd)
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax_number)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_list_value("bday", contact.bday)
        self.change_list_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_list_value("aday", contact.aday)
        self.change_list_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_list_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for contact in wd.find_elements_by_name("entry"):
                cells = contact.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = contact.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

