import enum

"""
Cache keys and prefixes
"""
# Using enum class create enumerations
class UserType(enum.Enum):
    USER = "user"
    ADMIN = "admin"