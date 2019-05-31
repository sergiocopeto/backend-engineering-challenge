import unittest
from TranslationDeliveredEventTools.translation_delivered_event_tools.handlers.translation_delivered_event_handler import \
    TranslationDeliveredEventHandler
from TranslationDeliveredEventTools.translation_delivered_event_tools.features.average_delivery_time import \
    AverageDeliveryTime


class PackageTests(unittest.TestCase):

    def test_handler_load_incorrect_file_throws_exception(self):
        # arrange
        filename = 'badformat.json'

        # assert
        with self.assertRaises(Exception):
            handler = TranslationDeliveredEventHandler(filename)

    def test_average_delivery_time_feature_returns_correct_value(self):
        # arrange
        filename = 'events.json'
        expected_result = 35.0
        handler = TranslationDeliveredEventHandler(filename)

        # act
        result = AverageDeliveryTime.compute(handler.data)

        # assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
