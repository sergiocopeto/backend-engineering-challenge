# Unbabel Backend Engineering Challenge

This repository contains a tool for computing average translation times from a set of translation delivery events for a specified interval.

## Installation
To use this tool, please install all required packages using the following command:

```
pip install -r "requirements.txt"
```

## Usage

The script uses the following arguments:
* -i (--input_file): Path to the JSON file containing a stream of translation delivered events
* -w (--window_size): temporal window (in seconds) for average delivery time computation.

The script also outputs a JSON file containing the results 
