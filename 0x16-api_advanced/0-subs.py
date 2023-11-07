#!/usr/bin/python3
"""query subscribers on reddit api"""

import requests


def number_of_subscribers(subreddit):
    """return number of subcribers on reddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set a custom User-Agent to identify your application
    headers = {
        "User-Agent": "MyRedditBot/1.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    return 0
