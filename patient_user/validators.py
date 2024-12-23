import re
from rest_framework.exceptions import ValidationError

# Used docstrings to describe the purpose of each validator then after imported them into the serializer


def validate_username(value):
    """username contains only alphanumeric characters."""
    if not value.isalnum():
        raise ValidationError("Username can only contain letters and numbers.")
    return value


def validate_email(value):
    """Ensure the email has a valid format."""
    if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
        raise ValidationError("Enter a valid email address.")
    return value


def validate_phone_number(value):
    """Ensure the phone number is valid."""
    phone_pattern = re.compile(r"^(?:07\d{8}|0\d{9}|\+254\d{9})$")
    if not phone_pattern.match(value):
        raise ValidationError(
            "Phone number must start with '07', '0', or '+254' and contain a valid number of digits."
        )
    return value


def validate_password(value):
    """Ensure the password meets complexity requirements."""
    if (
        len(value) < 8
        or not any(char.isdigit() for char in value)
        or not any(char.isalpha() for char in value)
    ):
        raise ValidationError(
            "Password must have at least 8 characters long, contain at least one letter, and one number."
        )
    return value
