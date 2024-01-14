from unittest import TestCase
from unittest.mock import patch
from src.twitter import sendTweet
import tweepy

class TestTwitter(TestCase):
    @patch('tweepy.Client')
    def test_sendTweet(self, mock_Client):
        # Arrange
        api_key = 'your_api_key'
        api_secret = 'your_api_secret'
        access_token = 'your_access_token'
        token_secret = 'your_token_secret'
        message = 'Test tweet message'

        # Mock the client and create_tweet method
        mock_client_instance = mock_Client.return_value
        mock_tweet = mock_client_instance.create_tweet.return_value

        # Act
        result = sendTweet(api_key, api_secret, access_token, token_secret, message)

        # Assert
        mock_Client.assert_called_once_with(consumer_key=api_key, consumer_secret=api_secret, access_token=access_token, access_token_secret=token_secret)
        mock_client_instance.create_tweet.assert_called_once_with(text=message, user_auth=True)
        self.assertEqual(result, mock_tweet)