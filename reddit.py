import requests


class Reddit:

    def get_popular_videos(self):
        url = "https://www.reddit.com/r/gifs/top.json?t=day"
        response = requests.get(url, headers={'User-agent': 'netology'})
        return response.json()
