#!/usr/bin/python3
""" """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        data = res.read()
    print(f"""Body response:
    - type: {type(data)}
    - content: {data}
    - utf8 content: {data.decode("utf8")}""")
