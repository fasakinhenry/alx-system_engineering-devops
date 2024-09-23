#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
    # Define the API URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set the custom User-Agent to avoid Reddit API rate-limiting
    headers = {"User-Agent": "My-User-Agent"}

    # Make the GET request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the status code indicates success (200 OK)
    if response.status_code == 200:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    else:
        # If the subreddit is invalid or any error occurs, return 0
        return 0
