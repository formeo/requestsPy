from pprint import pprint

import requests

from reddit import Reddit
from ya_disk import YandexDisk

TOKEN = ""


def test_request():
    url = "https://bootssizes/get"
    params = {"model": "nike123"}
    headers = {"Authorization": "secret - token - 123"}
    response = requests.get(url, params=params, headers=headers, timeout=5)
    pprint(response)


if __name__ == '__main__':
    reddit = Reddit()
    pprint(reddit.get_popular_videos())
    ya = YandexDisk(token="")
    ya.upload_file_to_disk("test/netology", "test.txt")
