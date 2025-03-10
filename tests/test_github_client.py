# import unittest


# class TestGitHubClient(unittest.TestCase):
#     def test_fetch_updates(self):
#         pass
        

# if __name__ == '__main__':
#     unittest.main()



import sys
sys.path.append('.')
from src.github_client import GitHubClient
from src.config import Config
from src.subscription_manager import SubscriptionManager

config = Config()
github_client = GitHubClient(config.github_token)
subscription_manager = SubscriptionManager(config.subscriptions_file)

print(github_client.fetch_updates(subscription_manager.get_subscriptions()))