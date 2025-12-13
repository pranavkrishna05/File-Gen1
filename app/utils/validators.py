import re
from app.utils.errors import ValidationError

EMAIL_REGEX = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

PASSWORD_MIN_LENGTH = 8
PASSWORD_COMPLEXITY = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$'


def validate_email(email: str) -> None:
    """
    Validates email format.

    :param email: Email to validate
    :raises ValidationError: if email is invalid
    """
    if not re.match(EMAIL_REGEX, email):
        raise ValidationError("Invalid email format.")


def validate_password(password: str) -> None:
    """
    Validates password for minimum length and complexity.

    :param password: Password to validate
    :raises ValidationError: if password is invalid
    """
    if len(password) < PASSWORD_MIN_LENGTH:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.match(PASSWORD_COMPLEXITY, password):
        raise ValidationError("Password must include at least one uppercase letter, one lowercase letter, and one digit.")
