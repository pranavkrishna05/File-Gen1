import os

class MailConfig:
    """
    Configuration for Flask-Mail.
    """
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.example.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true") == "true"
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "false") == "true"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "your_username")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "your_password")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", "no-reply@example.com")

"""
This configuration file provides the necessary settings for Flask-Mail to send emails.
Ensure environment variables are set correctly.
"""