#!/usr/bin/python3
"""Login to my github using github API and print my id"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    pwd = sys.argv[2]

    res = requests.get(url, auth=HTTPBasicAuth(username, pwd))
    print(res.json().get("id"))
