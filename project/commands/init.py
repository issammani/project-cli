"""The init command."""


from json import dumps

from .base import Base



class Init(Base):
    """Say hello, world!"""

    def run(self):
        print('Hello , world')