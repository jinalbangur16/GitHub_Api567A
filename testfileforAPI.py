import unittest
import json
import re
from github_api import Git_Hub

class TestGitHubAPI(unittest.TestCase):
    """ Test cases for GitHub API """

    def test_repository_commit_summary(self):
        github = Git_Hub("jinalbangur16")

        self.assertEqual(github.summary(), [
            'Repo: 567B Number of commits: 7'
        ])

    def test_no_commit_summary(self):
        github = Git_Hub("jinalbangur16")

        self.assertEqual(github.summary(), [
            'Repo: 567B Number of commits: 7'
        ])

    def test_no_repositories_summary(self):
        github = Git_Hub("jinalbangur16")

        self.assertEqual(github.summary(), [])

if __name__ == "__main__":
    print("Running unit tests")
    unittest.main(exit=False, verbosity=2)