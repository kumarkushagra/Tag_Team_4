import pandas as pd

def update_csv(file_path,  uhid_value,  change_value):
    """
    Updates a CSV file by changing a specified column value for a given UHID.
    
    Parameters:
    file_path (str): The path to the CSV file.
    uhid_column (str): The name of the column containing UHID values.
    uhid_value (str): The UHID value to find in the CSV file.
    change_column (str): The name of the column to update.
    change_value: The new value to set in the change column.
    
    Returns:
    str: A confirmation message indicating the update was successful.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Find the index of the row with the specified UHID value
    row_index = df.index[df['Patient ID (UHID)'] == uhid_value].tolist()
    
    if not row_index:
        raise ValueError(f"UHID value {uhid_value} not found in column {uhid_column}.")
    
    # Update the specified column in the located row
    df.at[row_index[0], 'Uploaded'] = change_value
    
    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

    return f"Updated {'Uploaded'} for UHID {uhid_value} to {change_value}."

# Example usage:
if __name__=="__main__":
    file_path = 'C:/Users/EIOT/Desktop/Final.csv'
    # uhid_column = 'Patient ID (UHID)'  # Assuming 'Patient ID (UHID)' is the column name for UHID
    uhid_value = '500261504'  # Example: UHID value to search for
    # change_column = 'Uploaded'  # Column to update
    change_value = '1'  # New value for 'Uploaded' column

    try:
        message = update_csv(file_path,  uhid_value, change_value)
        print(message)
    except ValueError as e:
        print(f"Error: {str(e)}")
