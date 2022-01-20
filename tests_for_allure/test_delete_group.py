import random

from model.group import Group
from random import randrange
import allure


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("Given a selected group"):
        group = random.choice(old_groups)
    with allure.step("When I delete the group"):
        app.group.delete_group_by_id(group.id)
    with allure.step("Then the new group list is equal to the old list with the deleted group"):
        assert len(old_groups) - 1 == app.group.count()
        old_groups.remove(group)
        new_groups = db.get_group_list()
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
