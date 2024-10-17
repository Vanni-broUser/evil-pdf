from enum import Enum


class BaseEnum(Enum):

  @classmethod
  def get_enum_option(cls, value):
    return next((p for p in cls if p.value == value), None)
