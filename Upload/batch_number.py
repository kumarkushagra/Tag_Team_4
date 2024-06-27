import pandas as pd

import csv
import datetime

def latest_batch_number():
    csv_file_path = 'Database/mapping.csv'

    try:
        # Open the CSV file
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Initialize variables to track the latest batch and time
            latest_time = datetime.datetime.min
            latest_batch = None
            latest_normal_number = 0
            
            # Flag to check if there are any data rows
            has_data = False
            
            for row in reader:
                has_data = True
                # Combine date and time into a single datetime object
                timestamp = f"{row['date']} {row['Time']}"
                current_time = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
                
                # Compare current time with the latest time
                if current_time > latest_time:
                    latest_time = current_time
                    latest_batch = row['batch_no']
                    
                    # Extract the integer part of the normal name if it starts with 'Normal_'
                    if row['name_of_StudyID'].startswith('Normal_'):
                        latest_normal_name = row['name_of_StudyID']
                        latest_normal_number = int(''.join(filter(str.isdigit, latest_normal_name)))
            
            # If there were no data rows, return 0
            if not has_data:
                return 0, 0
            
            # Extract the integer part of the batch number
            latest_batch_number = int(''.join(filter(str.isdigit, latest_batch)))
            
            return latest_batch_number, latest_normal_number
    
    except FileNotFoundError:
        # Return 0 if the file is not found
        return 0, 0



if __name__=="__main__":
    latest_batch_number,normal_number = latest_batch_number()
    print(f"Batch Number: {latest_batch_number} and latest_normal number: {normal_number}")

