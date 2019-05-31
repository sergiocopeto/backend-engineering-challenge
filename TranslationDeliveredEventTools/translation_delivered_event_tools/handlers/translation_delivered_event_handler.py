import pandas as pd
from datetime import datetime


class TranslationDeliveredEventHandler:
    """
    This class serves as an handler for a translation delivered event stream
    """
    def __init__(self, filename: str):
        """
        Class constructor, for now used to open a local file
        :param filename:
            Path to the file containing a translation delivered event stream (in JSON format)
        """
        self.data = pd.read_json(filename)
        if 'timestamp' not in self.data or 'duration' not in self.data:
            raise Exception('JSON file does not contain required fields')

    def get_stream_start_time(self, rounded: bool = False) -> datetime:
        """
        Returns lowest timestamp in the data stream
        :param rounded:
            Boolean used to indicate whether output of this method should me rounded to the floor second of the timestamp
        :return:
            Lowest timestamp in the data stream (start time)
        """
        return self.data.timestamp.min() if not rounded else self.data.timestamp.dt.floor('1T').min()

    def get_stream_end_time(self, rounded: bool = False) -> datetime:
        """
        Returns highest timestamp in the data stream
        :param rounded:
            Boolean used to indicate whether output of this method should me rounded to the floor ceiling of the timestamp
        :return:
            Highest timestamp in the data stream (end time)
        """
        return self.data.timestamp.max() if not rounded else self.data.timestamp.dt.ceil('1T').max()

    def get_events_for_interval(self, start_time: datetime, end_time: datetime) -> datetime:
        """
        This method returns a subset of the gathered data, with the timestamps between start_time and end_time
        :param start_time:
            Lower limit timestamp for the subset retrieval
        :param end_time:
            Higher limit timestamp for the subset retrieval
        :return:
            Subset of the gathered data, with the timestamps between start_time and end_time
        """
        return self.data[(self.data['timestamp'] >= start_time) & (self.data['timestamp'] <= end_time)]
