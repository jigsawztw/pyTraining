# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group

import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(login="admin", password="secret")
    app.create_group(Group(name="my_group_name", header="header1", footer="footer1"))
    app.logout()


def test_add_group_empty(app):
    app.login(login="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
