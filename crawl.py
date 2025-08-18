from urllib.parse import urlparse


def normalize_url(input_url: str) -> str:
    """
    Check an input URL (string) an normalize it into some standard format. In our case, we will remove the https:// at the beginning of the url, and the / at the end.

    Args:
        input_url (str): An arbitrary url.

    Returns:
        normalized_url (str): The same url but normalized to our convention
    """
    # Suite of basic input checks
    if not isinstance(input_url, str):
        raise TypeError("Expected a string input")
    if input_url == "":
        raise ValueError("An empty string is not a url")

    # Store the url as its separate parts in url_object
    url_object = urlparse(input_url)

    # Perform some clean-up to return it in our wanted format (netloc/path)
    netloc = (url_object.netloc).lower()
    path = (url_object.path).lower()
    # Knock off the trailing / on the path if it exists
    split_path = list(path)

    if path == "/":
        path = ""

    elif split_path[-1] == "/":
        split_path.pop(-1)
        path = "".join(split_path)

    normalized_url = netloc + path
    return normalized_url
