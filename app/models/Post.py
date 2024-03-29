from datetime import datetime
from app.db import Base
from .Like import Like
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property

class Post(Base):
    __tablename__='posts'
    id= Column(Integer, primary_key=True)
    title= Column(String(100), nullable=False)
    post_url= Column(String(100), nullable= False)
    user_id= Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User')
    comments = relationship('Comment', cascade='all, delete')

    like_count = column_property(
        select(func.count(Like.id)).filter(Like.post_id == id)
    )

    likes = relationship('Like', cascade='all,delete')


