import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3"
                           " from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home_phone, mobile_phone, work_phone, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                                    phone2=phone2, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def get_groups_without_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list where group_id not in (select group_id from address_in_groups)")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=str(id), name=name))
        finally:
            cursor.close()
        return list

    def get_contacts_not_in_any_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook " 
                           "where id not in (select id from address_in_groups)")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contacts_in_group(self, num):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"select id from address_in_groups where group_id = '{num}'")
            for row in cursor:
                (id) = row
                list.append(Contact(id=str(id)))
        finally:
            cursor.close()
        return list

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    # def get_contacts_not_in_group(self, group):
    #     orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
    #     return self.convert_contacts_to_model(
    #         select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
    #
    # def get_groups_with_contact(self, contact):
    #     orm_contact = list(select(c for c in ORMFixture.ORMContact if c.id == contact.id))[0]
    #     return self.convert_groups_to_model(orm_contact.groups)
    #
    # def get_groups_without_contact(self, contact):
    #     orm_contact = list(select(c for c in ORMFixture.ORMContact if c.id == contact.id))[0]
    #     return self.convert_groups_to_model(select(c for c in ORMFixture.ORMGroup if orm_contact not in c.contacts))