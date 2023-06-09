from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, full_name=None, all_emails=None, all_phones_from_home_page=None, nickname=None, title=None, company=None, address=None, home=None, mobile=None, work=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, id=None, phone2=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.id = id
        self.phone2 = phone2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.full_name = full_name
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s %s"% (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.compare_with_None_values(self.firstname, other.firstname) and self.compare_with_None_values(self.lastname,other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def compare_with_None_values(self,value1,value2):
        if value1 == value2:
            return True
        if value1 is None and value2 == "":
            return True
        if value2 is None and value1 == "":
            return True
        return False