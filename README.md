# FIT to CSV Converter

A simple Python utility that converts Garmin FIT (Flexible and Interoperable Data Transfer) files to CSV format.

## Overview

The FIT file format is a binary file format used by Garmin fitness devices to store activity data such as GPS coordinates, heart rate, cadence, power, etc. This utility allows you to easily convert these files to CSV format for analysis in spreadsheet applications or other data processing tools.

## Requirements

- Python 3.6 or higher
- fitparse library

## Installation

1. Clone this repository or download the script
2. Install the required dependencies:

```
pip install fitparse
```

## Usage

### Command Line

```
python fit_to_csv.py input.fit [output.csv]
```

- `input.fit`: Path to the input FIT file (required)
- `output.csv`: Path to save the output CSV file (optional)
  - If not specified, the output file will be created with the same name as the input file but with a .csv extension

### As a Module

You can also import and use the conversion function in your own Python scripts:

```python
from fit_to_csv import convert_fit_to_csv

# Convert a FIT file to CSV
convert_fit_to_csv('path/to/input.fit', 'path/to/output.csv')
```

## Example

```
python fit_to_csv.py Afternoon_Ride.fit
```

This will create `Afternoon_Ride.csv` with all the data from the FIT file.

## Features

- Converts all data records from FIT files to CSV
- Automatically determines all available fields
- Maintains consistent column ordering
- Simple command-line interface
- Can be used as a standalone script or imported as a module

## File Format

The resulting CSV file contains all data points from the FIT file's "record" messages, with each field represented as a column.

## License

This project is open source and available for any use.

## Contact

For questions or issues, please open an issue on the project repository.