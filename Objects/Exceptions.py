# define Python user-defined exceptions
class UsernameUnavailableException(Exception):
    """Base class for other exceptions"""
    pass


class EmailUnavailableException(Exception):
    """Raised when the input value is too small"""
    pass


class PasswordHashException(Exception):
    """Raised when the input value is too large"""
    pass
