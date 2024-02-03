#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'YourAppName/1.0'}

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    elif response.status_code == 404:
        # Invalid subreddit, return 0
        return 0
    else:
        # Other error, print the status code and return 0
        print(f"Error: {response.status_code}")
        return 0
