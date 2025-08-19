import unittest
from crawl import normalize_url, get_urls_from_html


class TestCrawl(unittest.TestCase):
    # Tests for the normalize_url() function in crawl.py
    def test_NORMALIZE_URL_base_functionality(self):
        input_url = "https://blog.boot.dev/path/"

        actual_output = normalize_url(input_url)
        expected_output = "blog.boot.dev/path"

        self.assertEqual(actual_output, expected_output)

    def test_NORMALIZE_URL_no_path(self):
        input_url = "https://blog.boot.dev/"

        actual_output = normalize_url(input_url)
        expected_output = "blog.boot.dev"
        self.assertEqual(actual_output, expected_output)

    def test_NORMALIZE_URL_uppercase_domain(self):
        input_url = "https://blog.BOOT.dev/Path"

        actual_output = normalize_url(input_url)
        expected_output = "blog.boot.dev/path"
        self.assertEqual(actual_output, expected_output)

    def test_NORMALIZE_URL_no_prefix(self):
        input_url = "https://boot.dev/Path"

        actual_output = normalize_url(input_url)
        expected_output = "boot.dev/path"
        self.assertEqual(actual_output, expected_output)

    def test_NORMALIZE_URL_empty_string(self):
        with self.assertRaises(ValueError):
            normalize_url("")

    def test_NORMALIZE_URL_wrong_type_input(self):
        for bad_input in [123, None, 3.14, ["list"], {"dict": "value"}]:
            with self.assertRaises(TypeError):
                normalize_url(bad_input)

    # Tests for the get_urls_from_html function
    def test_GET_URLS_FROM_HTML_base_functionality(self):
        input_url = "http://www.ubuntu.com"
        sample_html = """<!DOCTYPE HTML><html><body lang="en" dir="ltr"><div id="wrapper" class="hfeed">
        <div id="header">
            <ul id="mothership">
                <li> <a href="/partners">Partners</a> </li>
                <li> <a href="http://www.ubuntu.com/partners">Partners</a> </li>
                <li> <a href="http://www.ubuntu.com/support">Support</a> </li>
                <li> <a href="http://www.ubuntu.com/community">Community</a> </li>
                <li> <a href="http://www.ubuntu.com">Ubuntu.com</a> </li>
            </ul></body></html>"""

        actual_output = get_urls_from_html(sample_html, input_url)
        expected_output = [
            "http://www.ubuntu.com/partners",
            "http://www.ubuntu.com/support",
            "http://www.ubuntu.com/community",
            "http://www.ubuntu.com",
        ]
        self.assertEqual(set(actual_output), set(expected_output))

    def test_GET_URLS_FROM_HTML_relative_urls_to_absolute_urls(self):
        input_url = "https://blog.boot.dev"
        input_body = "<html><body><a href='/partners'>Partners</a></body></html>"

        actual_output = get_urls_from_html(input_body, input_url)
        expected_output = ["https://blog.boot.dev/partners"]
        self.assertEqual(actual_output, expected_output)

    def test_GET_URLS_FROM_HTML_repeated_urls(self):
        input_url = "https://blog.boot.dev"
        input_body = "<html><body><a href='https://blog.boot.dev'><span>Boot.dev</span></a><a href='https://blog.boot.dev'><span>Boot.dev</span></a></body></html>"

        actual_output = get_urls_from_html(input_body, input_url)
        expected_output = ["https://blog.boot.dev"]
        self.assertEqual(actual_output, expected_output)

    def test_GET_URLS_FROM_HTML_case_sensitivity(self):
        input_url = "https://blog.boot.dev"
        input_body = "<html><body><A href='https://blog.boot.dev'><span>Boot.dev</span></a></body></html>"

        actual_output = get_urls_from_html(input_body, input_url)
        expected_output = ["https://blog.boot.dev"]
        self.assertEqual(actual_output, expected_output)

    def test_GET_URLS_FROM_HTML_empty_string(self):
        input_url = "https://blog.boot.dev"

        with self.assertRaises(ValueError):
            get_urls_from_html("", input_url)

    def test_GET_URLS_FROM_HTML_wrong_type_input(self):
        for bad_input1 in [123, None, 3.14, ["list"], {"dict": "value"}]:
            for bad_input2 in [123, None, 3.14, ["list"], {"dict": "value"}]:
                with self.assertRaises(TypeError):
                    get_urls_from_html(bad_input1, bad_input2)


if __name__ == "__main__":
    unittest.main()
