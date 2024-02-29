#!/usr/bin/python3
"""
sends a post request using data from a letter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        data = {"q": ""}
    else:
        data = {"q": sys.argv[1]}
    url = "http://0.0.0.0:5000/search_user"

    res = requests.post(url, data=data)

    try:
        result = res.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
