#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url)
    commits = res.json()
    for i in commits[:10]:
        sha = i.get('sha')
        author = i.get("commit").get("author").get('name')
        print("{}: {}".format(sha, author))

