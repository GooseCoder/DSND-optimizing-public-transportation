"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """ The Weather model class"""

    def __init__(self):
        """ Instantiates the weather object"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """ Process the weather data"""
        data = message.value()
        self.temperature = data["temperature"]
        self.status = data["status"]


