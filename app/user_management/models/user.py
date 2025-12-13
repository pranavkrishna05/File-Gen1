from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    """
    Represents a user domain object with attributes enforced by validation criteria.
    """
    email: EmailStr = Field(..., description="Unique email address of the user.")
    password: str = Field(..., min_length=8, max_length=128, description="Password for the user account with complexity requirements.")

    def __str__(self) -> str:
        return f"User(email={self.email})"
