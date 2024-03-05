#!/usr/bin/python3
"""
queries to https://www.reddit.com/dev/api/
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    domain = 'https://www.reddit.com'
    path = '/r/{}/about.json'.format(subreddit)
    url = '{}{}'.format(domain, path)
    header = {
        'user-agent': '0x16-api_advanced:project/v1.0.0 (by /u/chukwudinwabia42)',
        'over18': 'yes'
    }
    res = requests.get(
        url,
        headers=header,
        allow_redirects=False
    )
    code = res.status_code
    if code >= 300:
        return 0
    data = res.json().get('data')
    subs = data.get('subs')
    return subs
