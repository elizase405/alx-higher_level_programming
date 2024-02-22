#!/usr/bin/python3
"""print value of the X-Request-Id variable found in the header"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        header = res.headers
        _id = header.get("X-Request-Id")

    print(_id)
