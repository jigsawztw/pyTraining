# -*- coding: utf-8 -*-
__author__ = "Iv.Osipov"

# метод удаляет первую в списке групп группу
def test_delete_first_group(app):
    app.session.login(login="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()