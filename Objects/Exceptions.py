# define Python user-defined exceptions
class UsernameUnavailableException(Exception):
    """Raised when username is already taken"""
    pass

class EmailUnavailableException(Exception):
    """Raised when email is already taken"""
    pass

class PasswordHashException(Exception):
    """Raised when password hash fails"""
    pass

class PasswordLengthTooSmall(Exception):
    """Raised when requested password length is too small"""
    """Minimum size will be 4"""
    pass

class PasswordLengthTooLarge(Exception):
    """Raised when requested password length is too large"""
    """Maximum size will be 24"""
    pass
