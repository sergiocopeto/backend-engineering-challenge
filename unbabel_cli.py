"""
This script parses a stream of TranslationDelivered events, in JSON format, and computes a minute-by-minute average
of the delivery times for the last X minutes

Parameters:
    -i (--input_file): path to the input JSON file
    -w (--window_size): Window size (in minutes) for average delivery time computation
"""

import argparse
import json
from datetime import timedelta

from translation_delivered_event_tools.handlers.translation_delivered_event_handler import TranslationDeliveredEventHandler
from translation_delivered_event_tools.features.average_delivery_time import AverageDeliveryTime

parser = argparse.ArgumentParser(description='Message processing time computation')
parser.add_argument('-i', '--input_file', dest='input_file', required=True)
parser.add_argument('-w', '--window_size', dest='window_size', required=False, default=10)

args = parser.parse_args()

filename = args.input_file
window_size = int(args.window_size)

if not filename.endswith('.json'):
    print('Input file must be in JSON format')


# initialize the event handler
try:
    handler = TranslationDeliveredEventHandler(filename)
except():
    quit()

# use the handler to get the start and end timestamps to be used in the average computation cycle
start_timestamp = handler.get_stream_start_time(rounded=True)
end_timestamp = handler.get_stream_end_time(rounded=True)

# Set the starting point for the
current_timestamp = start_timestamp

output = []

# Main computation cycle
while current_timestamp <= end_timestamp:
    # compute the lowe bound fot the events subset
    low_bound = current_timestamp - timedelta(minutes=window_size)
    # get the events subset for the timestamp limits defined
    events_in_delta = handler.get_events_for_interval(low_bound, current_timestamp)
    # compute the average translation duration
    mean_duration = AverageDeliveryTime.compute(events_in_delta)
    # print values in the console and keep them for further export in JSON format
    print(current_timestamp, mean_duration)
    output.append({'date': str(current_timestamp), 'average_delivery_time': mean_duration})
    # prepare the next computation cycle
    current_timestamp = current_timestamp + timedelta(minutes=1)

# Write the output results in a separate JSON file
with open(str(start_timestamp).replace(':', '') + '_' + str(end_timestamp).replace(':', '') + '.json', 'w') as f:
    json.dump(output, f)
