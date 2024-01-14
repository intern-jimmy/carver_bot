"""
from unittest import TestCase
from unittest.mock import patch, MagicMock
from web3 import Web3
from src.carver import carverAwayUntil, carverWorkingUntil, carverDataSet

class TestCarver(TestCase):
    def setUp(self):
        self.w3 = Web3()  # Instantiate a mock Web3 object
        self.contract = MagicMock()  # Instantiate a mock contract object

    @patch("carver.Web3")
    def test_carverAwayUntil(self, mock_web3):
        mock_web3.return_value = self.w3
        self.contract.functions.awayUntil().call.return_value = 123  # Set the expected return value

        result = carverAwayUntil(self.w3, self.contract)

        self.assertEqual(result, 123)
        self.contract.functions.awayUntil().call.assert_called_once()

    @patch("carver.Web3")
    def test_carverWorkingUntil(self, mock_web3):
        mock_web3.return_value = self.w3
        self.contract.functions.workingUntil().call.return_value = 456  # Set the expected return value

        result = carverWorkingUntil(self.w3, self.contract)

        self.assertEqual(result, 456)
        self.contract.functions.workingUntil().call.assert_called_once()

    @patch("carver.Web3")
    def test_carverDataSet(self, mock_web3):
        mock_web3.return_value = self.w3
        # Set the expected return values for the various functions
        self.contract.functions.awayUntil().call.return_value = 123
        self.contract.functions.getAvailability().call.return_value = (1, 2)
        self.contract.functions.minClosedTime().call.return_value = 789
        self.contract.functions.minOpenTime().call.return_value = 101
        self.contract.functions.paused().call.return_value = False
        self.contract.functions.varClosedTime().call.return_value = 111
        self.contract.functions.varOpenTime().call.return_value = 222
        self.contract.functions.workingUntil().call.return_value = 456

        with patch("builtins.print") as mock_print:
            carverDataSet(self.w3, self.contract)

            # Assert that the print statements are called with the expected values
            mock_print.assert_called_with(
                "away until: 123 \n get availability: (1, 2) \n min closed time: 789 \n min open time: 101 \n paused: False \n var closed time: 111 \n var open time: 222 \n working until: 456"
            )
"""