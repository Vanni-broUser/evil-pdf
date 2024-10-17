import enum
from datetime import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, func


Base = declarative_base()


class BaseEntity(Base):
  __abstract__ = True

  id = Column(Integer, primary_key=True, autoincrement=True)
  created_at = Column(DateTime(timezone=True), default=func.now())
  updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

  def to_dict(self):
    dict_obj = {}
    for attribute in self.__dict__:
      if getattr(self, attribute) is not None and attribute != '_sa_instance_state':
        dict_obj[attribute] = getattr(self, attribute)
        if isinstance(dict_obj[attribute], enum.Enum):
          dict_obj[attribute] = dict_obj[attribute].value
        elif type(dict_obj[attribute]) is datetime:
          dict_obj[attribute] = dict_obj[attribute].strftime('%d/%m/%Y %H:%M')
    return dict_obj

  def __repr__(self):
    attributes = [f'{attr}: {getattr(self, attr)}' for attr in self.to_dict()]
    return f'{self.__class__.__name__} {{{", ".join(attributes)}}}'
