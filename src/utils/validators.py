def is_valid_email(email):
    """Validate the email format."""
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def is_non_empty_string(value):
    """Check if the value is a non-empty string."""
    return isinstance(value, str) and bool(value.strip())

def validate_artist_data(name, genre, contact_info):
    """Validate artist data before adding to the database."""
    if not is_non_empty_string(name):
        raise ValueError("Artist name must be a non-empty string.")
    if not is_non_empty_string(genre):
        raise ValueError("Artist genre must be a non-empty string.")
    if not is_valid_email(contact_info):
        raise ValueError("Contact information must be a valid email address.")
    return True