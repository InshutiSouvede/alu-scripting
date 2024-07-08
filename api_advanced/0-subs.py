#!/usr/bin/python3

"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid 'Too Many Requests' error
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Construct the URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
