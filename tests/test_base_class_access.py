# -*- coding: utf-8 -*-

from sensirion_driver_support_types.base_class_access import AccessBase


class Abase:

    def __init__(self):
        self._name = 'a_name'

    def get_name(self):
        return 'a_base'

    @staticmethod
    def static_fun():
        return 'a_static_fun'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


class Bbase:
    def get_name(self):
        return 'b_base'

    @classmethod
    def class_fun(cls):
        return 'b_class_fun'

    @staticmethod
    def static_fun():
        return 'b_static_fun'

class Single(Abase):
    base = AccessBase()


class Multiple(Abase, Bbase):
    a_base = AccessBase(Abase)
    b_base = AccessBase(Bbase)


def test_single_base_access():
    single = Single()
    assert single.base.get_name() == 'a_base'

def test_single_static_base_access():
    single = Single()
    assert single.base.static_fun() == 'a_static_fun'


def test_multiple_base_access():
    cls = Multiple()
    assert cls.a_base.get_name() == 'a_base'
    assert cls.b_base.get_name() == 'b_base'


def test_multiple_static_base_access():
    cls = Multiple()
    assert cls.a_base.static_fun() == 'a_static_fun'


def test_multiple_class_base_access():
    cls = Multiple()
    assert cls.a_base.static_fun() == 'a_static_fun'
    assert cls.b_base.class_fun() == 'b_class_fun'
