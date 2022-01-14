#!/usr/bin/python3
"""
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """create table"""
    rowid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    city = db.Column(db.String(200), nullable=False)

    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

    def serialize(self):
        return {
            "rowid": self.rowid,
            "name": self.name,
            "email": self.email,
            "city": self.city
        }
