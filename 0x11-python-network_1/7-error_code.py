#!/usr/bin/python3
"""
fetch a url and print data unless status code > 400
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    code = res.status_code

    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(res.text)
