# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(bank_data_filtered, filepath):    
    '''
    Writes a new csv file with the filtered bank data

    Args:
        bank_data_filtered (list of lists): The filtered bank data
    
    Returns no value
    '''
    csvpath = Path(filepath)   
    with open(csvpath, 'w', newline = '') as csvfile:  #create a new writable file
        csvwriter = csv.writer(csvfile)    #create a csvwriter
        header = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate'] #add the original header to the new file
        csvwriter.writerow(header)
        for row in bank_data_filtered:  #add the filtered loan data to the new file
            csvwriter.writerow(row)
