import sys
from crawl import get_html


def main():
    # Usage: uv run main.py base_url
    CLI_input = sys.argv

    # Basic CLI error handling
    if len(CLI_input) < 2:
        print("no website provided")
        sys.exit(1)
    elif len(CLI_input) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = str(CLI_input[1])
    print(f"starting crawl of: {base_url}")

    html = get_html(base_url)

    print(html)


if __name__ == "__main__":
    main()
