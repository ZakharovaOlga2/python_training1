from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1",name="addressbook",user="root",password="")
try:
    lst = db.get_contacts_not_in_group(Group(id="11"))
    for item in lst:
        print(item)
    print(len(lst))
finally:
    pass