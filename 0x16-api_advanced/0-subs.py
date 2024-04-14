#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import json
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    url = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit), headers={"User-Agent": "brianbryank"})
    if url.status_code == 200:
        return url.json().get("data").get("subscribers")
    else:
        return 0
