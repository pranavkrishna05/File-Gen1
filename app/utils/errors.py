class ValidationError(Exception):
    """
    Exception raised for validation errors in inputs such as email and password.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class RegistrationError(Exception):
    """
    Exception raised for errors during registration such as duplicate email.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
