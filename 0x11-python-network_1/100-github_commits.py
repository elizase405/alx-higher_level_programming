#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url)
    #for i in range(0, 10):
    for i in res.json():
        print("{}: {}".format(i.get('sha'), i.get('author').get('login')))
