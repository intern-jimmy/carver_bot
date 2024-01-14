from unittest import TestCase
from datetime import datetime, timedelta
from src.analysis import extractData, timeMessage

class TestCommands(TestCase):
    def test_extractData_working_true(self):
        current_time = datetime.now()
        carver_data = {
            "working": True,
            "workingUntil": current_time + timedelta(hours=2),
            "time": current_time
        }
        prev_carver_data = {
            "working": False,
            "awayUntil": current_time + timedelta(days=1),
            "time": current_time - timedelta(hours=2)
        }

        result = extractData(carver_data, prev_carver_data)

        self.assertEqual(result["working"], True)
        self.assertEqual(result["workingStatusChanged"], True)
        self.assertIsInstance(result["timeLeft"], timedelta)
        self.assertTrue(result["timeLeft"] > timedelta(0))

    def test_extractData_working_false(self):
        current_time = datetime.now()
        carver_data = {
            "working": False,
            "awayUntil": current_time + timedelta(days=1),
            "time": current_time
        }
        prev_carver_data = {
            "working": True,
            "workingUntil": current_time + timedelta(hours=2),
            "time": current_time - timedelta(hours=2)
        }

        result = extractData(carver_data, prev_carver_data)

        self.assertEqual(result["working"], False)
        self.assertEqual(result["workingStatusChanged"], True)
        self.assertIsInstance(result["timeLeft"], timedelta)
        self.assertTrue(result["timeLeft"] > timedelta(0))

    def test_timeMessage(self):
        data = {
            "days": 2,
            "hours": 3,
            "minutes": 45,
            "seconds": 30
        }

        result = timeMessage(data)

        self.assertEqual(result, "2 days 3 hours 45 minutes 30 seconds")

    def test_timeMessage_singular(self):
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 1,
            "seconds": 1
        }

        result = timeMessage(data)

        self.assertEqual(result, "1 day 1 hour 1 minute 1 second")
        data = {
            "days": 1,
            "hours": 1,
            "minutes": 1,
            "seconds": 1
        }

        result = timeMessage(data)

        self.assertEqual(result, "1 day 1 hour 1 minute 1 second")