# AUTOGENERATED! DO NOT EDIT! File to edit: 01_enum.ipynb (unless otherwise specified).

__all__ = ['FunctionalEnum', 'DocumentedEnum']

# Cell
import enum
from .typing import Member, Mem

# Cell
class _FunctionalMeta(enum.EnumMeta):
    "An enum metaclass with a better repr"
    def __repr__(cls): return f"<FunctionalEnum {cls.__name__}>"

# Cell
class FunctionalEnum(enum.Enum, metaclass=_FunctionalMeta):
    """
    An `Enum` class implementing `__ne__`, `__eq__`, and `__str__` to compare `self.value`.

    Compatible with the functional API.
    """
    def __str__(self): return str(self.value)
    def __eq__(self, other): return getattr(other, "value", other) == self.value
    def __ne__(self, other): return getattr(other, "value", other) != self.value

# Cell
class _DocumentedMeta(_FunctionalMeta):
    "An enum metaclass with a better repr"
    def __repr__(cls): return f"<DocumentedEnum {cls.__name__}>"

# Cell
class DocumentedEnum(FunctionalEnum, metaclass=_DocumentedMeta):
    """
    An `Enum` capabile of having its members have docstrings.

    Inherits `FunctionalEnum` to allow for logic comparison via `==`, `!=`,
    and string transformation of `self.value` via str(self).

    Docstrings must *always* be present when in use.

    Should be passed in the form of:
      value, docstring
    """
    def __init__(self, *args):
        if args[-1] is not None:
            self.__doc__ = args[-1]
        if len(args) > 1:
            self._value_ = args[0]
        else:
            self._value_ = None