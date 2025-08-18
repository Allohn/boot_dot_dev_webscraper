def normalize_url(input_url: str) -> str:
    """
    Check an input URL (string) an normalize it into some standard format. In our case, we will remove the https:// at the beginning of the url, and the / at the end.

    Args:
        input_url (str): An arbitrary url.

    Returns:
        normalized_url (str): The same url but normalized to our convention"""
    normalized_url = input_url

    return normalized_url
