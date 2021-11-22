# -*- coding: utf-8 -*-

from sensirion_driver_support_types.BaseClassAccess import AccessBase


class Abase:

    def __init__(self):
        self._name = 'a_name'

    def get_name(self):
        return 'a_base'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Bbase:
    def get_name(self):
        return 'b_base'


class Single(Abase):
    base = AccessBase()


class Multiple(Abase, Bbase):
    a_base = AccessBase(Abase)
    b_base = AccessBase(Bbase)


def test_single_base_access():
    single = Single()
    assert single.base.get_name() == 'a_base'


def test_multiple_base_access():
    cls = Multiple()
    assert cls.a_base.get_name() == 'a_base'
    assert cls.b_base.get_name() == 'b_base'
