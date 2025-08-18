import unittest
from crawl import normalize_url


class TestCrawl(unittest.TestCase):
    def test_strip_scheme_and_trailing_slashes_normalize_url(self):
        input_url = "https://blog.boot.dev/path/"

        actual_output = normalize_url(input_url)
        expected_output = "blog.boot.dev/path"

        self.assertEqual(actual_output, expected_output)

    def test_no_path(self):
        input_url = "https://blog.boot.dev/"

        actual_output = normalize_url(input_url)
        expected_output = "blog.boot.dev"
        self.assertEqual(actual_output, expected_output)

    def test_uppercase_domain(self):
        input_url = "https://blog.BOOT.dev/Path"

        actual_output = normalize_url(input_url)
        expected_output = "blog.boot.dev/path"
        self.assertEqual(actual_output, expected_output)

    def test_no_prefix(self):
        input_url = "https://boot.dev/Path"

        actual_output = normalize_url(input_url)
        expected_output = "blog.boot.dev/path"
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
