import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re

class DBFixture:
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
            cursor.execute("Select group_id, group_name,group_header,group_footer from group_list")
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
            cursor.execute("Select id,firstname,lastname,email,email2,email3,home,mobile,work,phone2,address from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, email, email2, email3, home, mobile, work, phone2, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,all_emails=merge_emails_like_home_page(email, email2, email3),
                                    address=address,all_phones_from_home_page=merge_phones_like_home_page(home,mobile,work,phone2)))
        finally:
            cursor.close()
        return list

    def get_contact_list_without_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("Select id,firstname,lastname from addressbook adr where deprecated='0000-00-00 00:00:00' and not exists(select * from address_in_groups gr where gr.id=adr.id);")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

def merge_emails_like_home_page(email,email2,email3):
    result = "\n".join(filter(lambda x : x != "",filter(lambda x : x is not None,
                                                               [email, email2, email3]
                                     )
                              )
              )
    if result is None:
          result=""
    return result

def merge_phones_like_home_page(home,mobile,work,phone2):
    result = "\n".join(filter(lambda x : x != "",map(lambda x:clear(x),
                                                        filter(lambda x : x is not None,
                                                               [home, mobile, work, phone2])
                                     )
                              )
              )
    if result is None:
          result=""
    return result

def clear(s):
    return re.sub("[() -+]","",s)
