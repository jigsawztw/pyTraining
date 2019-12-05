# -*- coding: utf-8 -*-
from model.group import Group

# Метод осуществляет вход в систему, создает группу с параметрами и проверяет ее наличие, затем выходит из системы
def test_add_group(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group(name="my_group_name", header="header1", footer="footer1"))
    app.session.logout()

# Метод осуществляет вход в систему, создает группу без параметров и проверяет ее наличие, затем выходит из системы
def test_add_group_empty(app):
    app.session.login(login="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
