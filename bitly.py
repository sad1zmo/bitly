import sys
import requests
from urllib.parse import urlparse
import json
import re
import bitly_token

access_token = bitly_token.access_token
create_bitlinks_url = "https://api-ssl.bitly.com/v4/bitlinks"


def is_valid_url(url):
    regex = r"(https?://)([a-zA-Z0-9_\-.]+)([a-zA-Z0-9/\-._~:/?#[\]@!$&'()*+,;=]+)?"
    return bool(re.match(regex, url))

def shorten_link(token, url):
  
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {
        "long_url": f"{url}"
    }

    response = requests.post(
        "https://api-ssl.bitly.com/v4/bitlinks", headers=headers, data=json.dumps(data)
    )
    
    response.raise_for_status()
    return response.json().get('link')

# Check URL 
while True:
    url_for_verification = input("Enter your URL address: ")
    if is_valid_url(url_for_verification):
        break
    else:
        print(f"Yours URL '{url_for_verification}' doesn't valid, chage it.")

parsed_url = urlparse(url_for_verification)
count_clicks_url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.hostname}{parsed_url.path}/clicks/summary"

def count_clicks(token, url):
    headers = {
    'Authorization': f'Bearer {token}',
    }

    params = {
    'unit': 'day',
    'units': '-1',
    }
    
    try:
        clicks_count = requests.get(url, headers=headers, params=params)
        clicks_count.raise_for_status()
        return clicks_count
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def is_bitlink(url):
    if parsed_url.hostname != "bit.ly":
        print(url)
        print('bitlink', shorten_link(access_token, url))
    else:
        count_clicks(access_token, count_clicks_url)
        
if __name__ == '__main__':
    is_bitlink(url_for_verification)
