import logging
from typing import Dict
from flask_mail import Mail, Message
from app.auth.models.user import User
from app.database.db import db
from app.utils.errors import RegistrationError
from app.utils.validators import validate_email, validate_password

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RegisterService:
    """
    Business logic for handling user registration.
    """
    def __init__(self):
        # Initialize Flask-Mail
        self.mail = Mail()

    def register_user(self, email: str, password: str) -> Dict[str, str]:
        """
        Handles user registration flow.

        Validates user details, creates account, and sends confirmation email.

        :param email: User email
        :param password: User password
        :return: Response dict upon completion
        """
        try:
            validate_email(email)
            validate_password(password)

            if User.query.filter_by(email=email).first():
                logger.warning(f"Email already in use: {email}")
                raise RegistrationError("Email address is already registered.")

            # Create new user instance
            new_user = User(email=email, password=User.hash_password(password))
            db.session.add(new_user)
            db.session.commit()

            self.send_confirmation_email(email)

            return {"message": "Registration successful. Confirmation email sent."}
        except Exception as e:
            logger.error(f"Error during registration: {e}")
            raise e

    def send_confirmation_email(self, email: str):
        """
        Sends confirmation email upon successful user creation.

        :param email: User email
        """
        try:
            message = Message(
                subject="Account Registration Confirmation",
                recipients=[email],
                body="Thank you for registering! Your account was successfully created."
            )
            self.mail.send(message)
            logger.info(f"Sent confirmation to {email}")
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            raise RegistrationError("Failed to send confirmation email.")