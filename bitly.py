import os
import argparse
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv

CREATE_BITLINKS_URL = "https://api-ssl.bitly.com/v4/bitlinks"


def create_parser():
    parser = argparse.ArgumentParser(
        description="передача ссылок пользователем"
    )
    parser.add_argument("-l", "--links", nargs="+", default=[])

    return parser


def shorten_link(token, url):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    long_url = {
        "long_url": url
    }

    response = requests.post(
        CREATE_BITLINKS_URL, headers=headers, json=long_url
    )

    response.raise_for_status()
    return response.json().get("link")


def count_clicks(token, url):
    parsed_url = urlparse(url)
    count_clicks_url = f"{CREATE_BITLINKS_URL}/{parsed_url.hostname}" \
        f"{parsed_url.path}/clicks/summary"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    params = {
        "unit": "day",
        "units": "-1",
    }

    clicks_count = requests.get(count_clicks_url, headers=headers,
                                params=params)
    clicks_count.raise_for_status()
    return clicks_count


def is_bitlink(token, url):
    parsed_url = urlparse(url)
    return_bitlink_information_url = f"{CREATE_BITLINKS_URL}/" \
        f"{parsed_url.hostname}{parsed_url.path}"

    headers = {
        "Authorization": f"Bearer {token}",
    }

    response = requests.get(return_bitlink_information_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    access_token = os.environ["BITLY_ACCESS_TOKEN"]
    args = create_parser().parse_args()
    if not args.links:
        url_for_verification = input("Enter your URL address: ")
        args.links.append(url_for_verification)
    for url_for_verification in args.links:
        if is_bitlink(access_token, url_for_verification):
            try:
                print(count_clicks(access_token, url_for_verification))
            except requests.RequestException as e:
                print(e)
        else:
            try:
                print(f"Bitlink for {url_for_verification}:  {shorten_link(
                    access_token, url_for_verification
                )}")
            except requests.RequestException as e:
                print(e)


if __name__ == '__main__':
    main()
