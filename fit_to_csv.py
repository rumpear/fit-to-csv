#!/usr/bin/env python3
"""
fit_to_csv.py - Convert FIT files to CSV format
Usage: python fit_to_csv.py input.fit [output.csv]
If no output file is specified, it will use the input filename with a .csv extension
"""

import sys
import csv
import os
from fitparse import FitFile


def convert_fit_to_csv(fit_file_path, csv_file_path=None):
    """
    Convert a FIT file to CSV format
    
    Args:
        fit_file_path: Path to the FIT file
        csv_file_path: Path to save the CSV file (optional)
    
    Returns:
        Path to the created CSV file
    """
    # If no CSV file path is provided, use the FIT file name with .csv extension
    if csv_file_path is None:
        csv_file_path = os.path.splitext(fit_file_path)[0] + '.csv'
    
    # Parse the FIT file
    try:
        fit_file = FitFile(fit_file_path)
        
        # Get all data messages that are of type "record"
        records = fit_file.get_messages('record')
        
        # Prepare data for CSV
        data = []
        
        # Get all possible field names first (headers for CSV)
        field_names = set()
        for record in records:
            for field in record:
                field_names.add(field.name)
        
        # Reset the messages iterator
        records = fit_file.get_messages('record')
        
        # Process each record and build data rows
        for record in records:
            row = {}
            for field in record:
                # Use the field name as key and its value as value
                row[field.name] = field.value
            data.append(row)
        
        # Sort field names for consistent column order
        field_names = sorted(list(field_names))
        
        # Write to CSV
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Successfully converted {fit_file_path} to {csv_file_path}")
        return csv_file_path
    
    except Exception as e:
        print(f"Error converting FIT file: {e}")
        return None


def main():
    # Check if enough arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python fit_to_csv.py input.fit [output.csv]")
        sys.exit(1)
    
    # Get input file path
    fit_file_path = sys.argv[1]
    
    # Get output file path if provided
    csv_file_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Convert FIT to CSV
    convert_fit_to_csv(fit_file_path, csv_file_path)


if __name__ == "__main__":
    main()