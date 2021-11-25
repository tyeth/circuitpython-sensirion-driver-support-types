# -*- coding: utf-8 -*-

from functools import partial
from typing import Optional, Type, Any
from inspect import isfunction


class AccessBase:
    """
    This class allows to declare names for mixin base classes. In this way the function from these base classes
    can be called with the syntax self.<name>.function() instead of mixin_class.function(self).
    """
    def __init__(self, base_class: Optional[Type[Any]] = None):
        """
        Initializes the access to the mixin class.

        In case only one base class is there, the base_class parameter can be omitted.
        """
        self._base_class = base_class
        self._name: Optional[str] = None
        self._instance: Optional[object] = None

    def __set_name__(self, instance, name):
        self._name = name
        self._instance = instance

    def __get__(self, instance, instance_type):
        self._instance_type = instance_type
        if self._base_class is None:
            return super(instance_type, instance)
        else:
            return self

    def __getattr__(self, item):
        """
        this will be called when a function call is issued on the base class
        :params item: name of the function that is accessed
        :return: if it's a member function the function is returned with the first argument bound to self or the
        respective base class
        else an exception is raised.
        """
        f = self._base_class.__dict__[item]
        if isfunction(f):
            return partial(f, self._instance)
        if isinstance(f, staticmethod) or isinstance(f, classmethod):
            return f.__get__(self._base_class)
        raise NotImplementedError("Base class access only implemented for methods, class and staticmethods")

