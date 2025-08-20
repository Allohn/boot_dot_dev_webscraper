import sys


def main():
    # Usage: uv run main.py base_url
    CLI_input = sys.argv

    if len(CLI_input) < 2:
        print("no website provided")
        sys.exit(1)
    elif len(CLI_input) > 2:
        print("too many arguments provided")
        base_url = str(CLI_input[1])
        sys.exit(1)
    else:
        base_url = str(CLI_input[1])
        print(f"starting crawl of: {base_url}")

    print("Hello from babies-first-webscraper!")


if __name__ == "__main__":
    main()
