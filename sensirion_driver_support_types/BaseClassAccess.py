# -*- coding: utf-8 -*-

from functools import partial
from typing import Optional, Type, Any


class _Base:
    def __init__(self, cls, instance, name):
        self._cls = cls
        self._instance = instance
        self._name = name

    def __getattr__(self, item):
        if item not in ['self', '_cls', '_instance', '_name', self._name]:
            return partial(self.cls.__dict__[item], self._instance)
        return super().__getattr__(item)


class AccessBase:
    def __init__(self, base_class: Optional[Type[Any]] = None):
        self._base_class = base_class
        self._name: Optional[str] = None
        self._instance: Optional[object] = None

    def __set_name__(self, owner, name):
        self._name = name
        self._instance = owner

    def __get__(self, instance, owner):
        if self._base_class is None:
            return super(owner, instance)
        else:
            return self

    def __getattr__(self, item):
        if item not in [self._name]:
            f = self._base_class.__dict__[item]
            if callable(f):
                return partial(f, self._instance)
            raise NotImplementedError()
        return self
