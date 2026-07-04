import re


def validate_name(name):
    """
    Name should contain only alphabets and spaces.
    """
    pattern = r"^[A-Za-z ]+$"

    if re.fullmatch(pattern, name):
        return True

    return False


def validate_email(email):
    """
    Validate email address using Regex.
    """
    pattern = r"^[\w.%+-]+@[\w.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(pattern, email):
        return True

    return False


def validate_phone(phone):
    """
    Phone number should start with
    6, 7, 8 or 9
    and contain exactly 10 digits.
    """
    pattern = r"^[6-9]\d{9}$"

    if re.fullmatch(pattern, phone):
        return True

    return False


def validate_cgpa(cgpa):
    """
    CGPA must be between 0 and 10.
    """

    try:

        cgpa = float(cgpa)

        if 0 <= cgpa <= 10:
            return True

        return False

    except ValueError:

        return False