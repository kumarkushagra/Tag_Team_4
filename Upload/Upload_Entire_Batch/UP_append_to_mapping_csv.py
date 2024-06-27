import csv
import os
import datetime
def append_to_csv(uhid, new_study_id,batch_no):
    current_datetime = datetime.datetime.now()

    # Store date and time in separate variables
    date = current_datetime.date()
    time = current_datetime.time()
    # by default, mapping.csv will be stored in Database dir
    user_csv_path = 'Database/mapping.csv'
    # Check if the CSV file exists
    csv_exists = os.path.exists(user_csv_path)
    
    # Define headers for the CSV file
    headers = ['uhid','date','Time', 'new_study_id','batch_no']
    
    # Open the CSV file in append mode
    with open('Database/mapping.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write headers only if the file was just created
        if not csv_exists:
            writer.writerow(headers)
        
        # Write the new data
        writer.writerow([uhid,date,time, new_study_id,batch_no])

if __name__ == "__main__":

    user_csv_path = 'Database/mapping.csv'
    uhid = '12345'
    new_study_id = 'study123'
    batch_name="Batch1"
    append_to_csv(uhid,new_study_id,batch_name)