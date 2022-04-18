from sqlalchemy import Column, String, Integer
from .Entity import Entity, Base

class User(Entity, Base):
    __tablename__ = 'Users'

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(Integer)

    def __init__(self, first_name, last_name, email, phone, created_by):
        Entity.__init__(self,created_by)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
