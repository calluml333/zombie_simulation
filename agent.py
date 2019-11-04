"""
Script that contains the Agent Class and relevant subclasses
"""


class Person:
  def __init__(self, name, postition):
    self.name = name
    self.age = postition

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isdigit():
            self.__name = value