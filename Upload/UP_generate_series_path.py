import os


def generate_all_series_path(batch_dir_path, uhid):
    """
    Returns a list of directories containing DICOM series for a given UHID.
    
    Parameters:
    unzip_dir_path (str): The path to the base directory containing UHID subdirectories.
    uhid (str): The UHID for which to return series directories.
    
    Returns:
    list: A list of paths to DICOM series directories.
    """
    series_dirs = []
    uhid_path = os.path.join(batch_dir_path, uhid)
    uhid_path = uhid_path.replace("\\", "/")

    # Check if the UHID directory exists
    if os.path.isdir(uhid_path):
        # Iterate over date directories
        for date_dir in os.listdir(uhid_path):
            date_path = os.path.join(uhid_path, date_dir)
            date_path = date_path.replace("\\", "/")

            if os.path.isdir(date_path):
                # Iterate over series directories
                for series_dir in os.listdir(date_path):
                    series_path = os.path.join(date_path, series_dir)
                    series_path = series_path.replace("\\", "/")

                    if os.path.isdir(series_path):
                        series_dirs.append(series_path)
    
    return series_dirs


if __name__=="__main__":
    unzip_dir_path="C:/Users/EIOT/Desktop/Unziped_dir"
    uhid="105325641"
    print(generate_all_series_path(unzip_dir_path,uhid))