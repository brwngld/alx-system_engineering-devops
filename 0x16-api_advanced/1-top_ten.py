#!/usr/bin/python3
"""Function to prints the titles of the first 10 hot posts
listed for a given subscribers on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given Reddit subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates success
    if response.status_code == 200:
        # Attempt to parse the JSON response
        try:
            data = response.json()
            # Check if the response contains valid data
            if data and 'data' in data:
                children = data['data'].get('children', [])
                # Print the titles of the posts
                for child in children:
                    post_data = child.get('data')
                    title = post_data.get('title')
                    print(title)
            else:
                print("No data found for subreddit:", subreddit)
        except ValueError:
            print("Error: Unable to parse JSON response")
    else:
        print("Error:", response.status_code)
