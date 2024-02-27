#!/usr/bin/python3
"""
post to a url
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = sys.argv[2]
    mydata = {"email": val}

    res = requests.post(url, data=mydata)
    print(res.text)
