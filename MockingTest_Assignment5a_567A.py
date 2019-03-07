import unittest
from unittest.mock import patch
import json
import re
from Mocking_Assignment5a_567A import Git_Hub


class Mocked_JSONReader:
    def __init__(self, test_data_path):
        self.__test_data_path = test_data_path

    def file_json_reader(self, path):
        if re.compile("users/[^/]+/repos").match(path):
            path = f"{self.__test_data_path}/repositories.json"
        elif re.compile("repos/[^/]+/567B/commit").match(path):
            path = f"{self.__test_data_path}/commit-567B.json"

        with open(path) as file:
            return json.load(file)


class TestGitHubAPI(unittest.TestCase):
    """ Test cases for GitHub API """

    @patch("github_api.GitHub._GitHub__http_json_reader")
    def test_repository_commit_summary(self, mocked):
        mocked.side_effect = Mocked_JSONReader(
            "test_data/with-repositories").file_json_reader

        github = Git_Hub("jinalbangur16")
        self.assertEqual(github.summary(), [
            'Repo: 567B Number of commits: 7'
        ])

    @patch("github_api.GitHub._GitHub__http_json_reader")
    def test_no_commit_summary(self, mocked):
        mocked.side_effect = Mocked_JSONReader(
            "test_data/with-repositories").file_json_reader

        github = Git_Hub("jinalbangur16")
        self.assertEqual(github.summary(), [
            'Repo: 567B Number of commits: 7'
        ])

    @patch("github_api.GitHub._GitHub__http_json_reader")
    def test_no_repositories_summary(self, mocked):
        mocked.side_effect = Mocked_JSONReader(
            "test_data/with-repositories").file_json_reader

        github = Git_Hub("jinalbangur16")
        self.assertEqual(github.summary(), [])


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main(exit=False, verbosity=2)
