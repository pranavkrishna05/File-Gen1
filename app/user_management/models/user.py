from app.utils.database import Base
from sqlalchemy import Column, String, Integer

class User {
    """
    Database model for a user.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
}
