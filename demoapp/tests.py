from django.test import TestCase
from datetime import datetime
from demoapp.models import Logger

class LoggerModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.logger = Logger.objects.create(
            first_name="John",
            last_name="McDonald"
        )
    
    def test_fields(self):
        self.assertIsInstance(self.logger.first_name, str)
        self.assertIsInstance(self.logger.last_name, int)
 
    def test_timestamps(self):
        self.assertIsInstance(self.logger.booking_time, datetime)

