#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'user-agent': '0x16-api_advanced:project/1.0 (by /u/chukwudinwabia42)',
        'over18': 'yes'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    print("Number of subscribers:", number_of_subscribers(subreddit))
