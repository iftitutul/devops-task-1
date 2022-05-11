#!/usr/bin/env python3

import requests
import sys

def main():
   print("Response code:", response_status_code(str(sys.argv[1])))

def response_status_code(site_url):
    redirect_url = input("Do you like to redirect (y/n): ").strip().lower()
    if redirect_url == 'y':
        response = requests.get(site_url, allow_redirects=True)
    elif redirect_url == 'n':
        response = requests.get(site_url, allow_redirects=False)
    else:
        response = requests.get(site_url, None)

    return response.status_code

if __name__ == "__main__":
    main()