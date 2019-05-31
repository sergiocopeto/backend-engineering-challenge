from pandas import DataFrame


class AverageDeliveryTime:
    """
    Class for computing the average delivery time from a set of translation delivered events
    """
    @staticmethod
    def compute(translation_delivered_events: DataFrame) -> float:
        """
        Static method to compute the average of the delivery times for a set of translation delivered events
        :param translation_delivered_events:
            DataFrame containing a set of translation delivered events
        :return:
            Average translation delivery time
        """
        return translation_delivered_events['duration'].mean() if len(translation_delivered_events) > 0 else 0
