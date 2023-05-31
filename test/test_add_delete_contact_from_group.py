from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app,db, orm):
    # проверка что контакты существуют
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Для добавления в группу"))
    # проверка что есть контакты не входящие в группы - можно иначе сделать(но у меня не работает добавление уже добавленных)
    if len(db.get_contact_list_without_groups()) == 0:
        app.contact.create(Contact(firstname="Для добавления в группу"))
    # проверка что группы существуют
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Сюда добавим контакт"))
    # берем первый без группы
    added_contact = db.get_contact_list_without_groups()[0]
    # берем группу, в которую добавляем контакт
    found_group_index = db.get_group_list()[0].id
    # сравнение и самое добавление
    old_list = orm.get_contacts_in_group(Group(id=found_group_index))
    old_list.append(added_contact)
    app.contact.add_contact_to_group(added_contact.id, found_group_index)
    new_list = orm.get_contacts_in_group(Group(id=found_group_index))
    assert sorted(new_list,  key=Contact.id_or_max) == sorted(old_list, key=Contact.id_or_max)

def test_delete_contact_from_group(app,db, orm):
    # проверка что группы существуют
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Сюда добавим контакт"))
    # проверка что контакты существуют
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Для добавления в группу"))
    # если нет контактов в группах - добавляем
    if len(db.get_contact_list_without_groups()) == len(db.get_contact_list()):
        test_add_contact_to_group(app,db, orm)
    for gr in db.get_group_list():
        if len(orm.get_contacts_in_group(Group(id=gr.id)))>0:
            found_group = gr.id
            found_contact = orm.get_contacts_in_group(Group(id=gr.id))[0]
            break
    old_list = orm.get_contacts_in_group(Group(id=found_group))
    app.contact.delete_contact_from_group(found_contact.id, found_group)
    new_list = orm.get_contacts_in_group(Group(id=found_group))
    new_list.append(found_contact)
    assert sorted(new_list, key=Contact.id_or_max) == sorted(old_list, key=Contact.id_or_max)