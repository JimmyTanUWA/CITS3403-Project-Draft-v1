from typing import Optional
from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_sqlalchemy import SQLAlchemy
import random


class movie(db.Model):
    name = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    tag = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(1000), nullable=True)
    rating = db.Column(db.String(10), nullable=True)
    release_date = db.Column(db.String(20),nullable=False)
    runtime = db.Column(db.String(20),nullable=False)
    plot = db.Column(db.String(1000),nullable=False)

    def __repr__(self) -> str:
        return f'moviedetails {self.name} {self.tag} {self.address} {self.rating} {self.release_date} {self.runtime} {self.plot}'

