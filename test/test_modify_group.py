# -*- coding: utf-8 -*-
from model.group import Group
__author__ = "Iv.Osipov"

def test_modify_group_name(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first_group(Group(name="new Group"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first_group(Group(header="new header"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.login(login="admin", password="secret")
    app.group.modify_first_group(Group(footer="footer"))
    app.session.logout()