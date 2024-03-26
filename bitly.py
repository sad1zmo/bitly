import sys
import os
import requests
from urllib.parse import urlparse
import json
import re
import bitly_token
from dotenv import load_dotenv


def shorten_link(token, url):
  
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    data = {
        "long_url": url
    }

    response = requests.post(
        create_bitlinks_url, headers=headers, json=data
    )
    
    response.raise_for_status()
    return response.json().get('link')

def count_clicks(token, url):
    headers = {
    'Authorization': f'Bearer {token}',
    }

    params = {
    'unit': 'day',
    'units': '-1',
    }
    
    clicks_count = requests.get(url, headers=headers, params=params)
    clicks_count.raise_for_status()
    return clicks_count

def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False
        
if __name__ == '__main__':
    load_dotenv()
    access_token = os.getenv("BITLY_ACCESS_TOKEN")
    create_bitlinks_url = "https://api-ssl.bitly.com/v4/bitlinks"

    while True:
        url_for_verification = input("Enter your URL address: ")
        try:
            response = requests.get(url_for_verification)
            response.raise_for_status()
            break
        except requests.RequestException:
            print(f"Yours URL '{url_for_verification}' doesn't valid, change it.")

    parsed_url = urlparse(url_for_verification)
    count_clicks_url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.hostname}{parsed_url.path}/clicks/summary"
    bitlink_info = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.hostname}{parsed_url.path}"

    chek_url_result = is_bitlink(access_token, bitlink_info)

    if chek_url_result:
        try:
            print(count_clicks(access_token, count_clicks_url))
        except requests.RequestException as e:
            print(e)
    else:
        print(f"Bitlink:  {shorten_link(access_token, url_for_verification)}")