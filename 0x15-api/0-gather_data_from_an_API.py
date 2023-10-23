#!/usr/bin/python3
""" Gather data from an API"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    to_do = requests.get(url + 'todos', params={'userId': sys.argv[1]}).json()
    completed = [title.get("title") for title in to_do if
                 title.get('completed') is True]
    print("Employee {} is done with tasks {}/{}):".format(user.get("name"),
                                                           len(completed),
                                                           len(to_do)))
    [print("\t {}".format(title)) for title in completed]
