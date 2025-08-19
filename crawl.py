from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# Sample page source
sample_html = """<!DOCTYPE HTML><html><body lang="en" dir="ltr"><div id="wrapper" class="hfeed">
<div id="header">
    <ul id="mothership">
        <li> <a href="http://www.ubuntu.com/partners">Partners</a> </li>
        <li> <a href="http://www.ubuntu.com/support">Support</a> </li>
        <li> <a href="http://www.ubuntu.com/community">Community</a> </li>
        <li> <a href="http://www.ubuntu.com">Ubuntu.com</a> </li>
    </ul></body></html>"""


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

    if path == "/":  # Check for an empty path/trailing slash of any kind, and remove it
        path = ""

    elif (
        split_path[-1] == "/"
    ):  # Check the characters in the path and knock off the last one if it's a trailing slash. Join back together
        split_path.pop(-1)
        path = "".join(split_path)

    normalized_url = netloc + path
    return normalized_url


def get_urls_from_html(html: str, base_url: str) -> list[str]:
    """
    Take in a HTML string, and a root url, and crawl the html to find links. Use the root_url to produce a list of absolute urls connected to the page

    Args:
        html (str): A html string
        base_url (str): An absolute url that is the root url of all the links on the page

    Returns:
        url_list list[str]: A list of un-normalized absolute urls.
    """

    # Suite of basic input checks
    if not (isinstance(base_url, str) and (isinstance(html, str))):
        raise TypeError("Expected a string input")
    if not base_url or not html:
        raise ValueError("An empty string is not a url")

    soup = BeautifulSoup(html, "lxml")  # Initialize the BS object with the lxml parser

    # Make a list of hrefs
    anchor_type = ["a", "A"]
    href_list = []

    for (
        a_type
    ) in (
        anchor_type
    ):  # For loop to make a check on both <a> and <A> in case of capitalization problems.
        anchor_list = soup.find_all(a_type)  # List of all anchor blocks
        for link in anchor_list:
            href_list.append(link.get("href"))

    # Check to make sure everything is absolute
    absolute_url_list = []
    for href in href_list:
        url_object = urlparse(href)

        # Split up the url into the network location and the path
        scheme = url_object.scheme
        netloc = url_object.netloc
        path = url_object.path

        if netloc == "":
            absolute_url_list.append(urljoin(base_url, path))
        else:
            absolute_url_list.append(scheme + "://" + netloc + path)

    # Check for duplicates
    absolute_url_list = list(set(absolute_url_list))

    return absolute_url_list
