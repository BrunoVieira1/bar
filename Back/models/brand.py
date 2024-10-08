from database.db import db
from sqlalchemy import Column, Integer, String, Float, Date,ForeignKey
from sqlalchemy.orm import relationship

class Brand(db.Model):
  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'idRequester': self.idRequester,
    }
  id = db.Column(Integer, primary_key=True)
  idRequester = db.Column(ForeignKey('user.id'))
  name = db.Column(String(100))

  requester = relationship('User', backref='brand')

  def __init__(self, name, idRequester):
    self.name = name
    self.idRequester = idRequester