#!/usr/bin/python3
"""querring reddit"""

import requests


def top_ten(subreddit):
    """Print the titles of top 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            "User-Agent": "MyRedditBot/1.0"
    }
    params = {
            "limit": 10
    }
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
    else:
        print("None")
        return
