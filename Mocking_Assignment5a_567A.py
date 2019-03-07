import unittest
import requests
from requests.exceptions import Timeout, RequestException


class Git_Hub:

    def __init__(self, username):
        self.__username = username
        self.__reader = self.__http_json_reader

    def __http_json_reader(self, url):
        try:
            response = requests.get("https://api.github.com/" + url)
        except (Timeout, RequestException) as e:
            raise e
        else:
            with response:
                return response.json()

    def repo(self):
        return self.__reader(f"users/{self.__username}/repos")

    def commit(self, repository):
        return self.__reader(f"repos/{self.__username}/{repository}/commit")

    def summary(self):
        return [f"Repo: {repository['name']} Number of commit: {len(self.commit(repository['name']))}" for repository in self.repo()]


if __name__ == "__main__":
    print(Git_Hub("jinalbangur16").summary())
