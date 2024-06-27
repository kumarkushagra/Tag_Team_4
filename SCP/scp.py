import paramiko
import os
 
def scp_transfer(
    source_host: str,
    source_user: str,
    source_file_path: str,
    dest_host: str,
    dest_user: str,
    dest_file_path: str,
    port: int
):
    temp_file = '/tmp/temp_file'
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Download file from source server
        ssh.connect(source_host, username=source_user, port=port)
        with ssh.open_sftp() as sftp:
            sftp.get(source_file_path, temp_file)
        ssh.close()
        # Upload file to destination server
        ssh.connect(dest_host, username=dest_user, port=port)
        with ssh.open_sftp() as sftp:
            sftp.put(temp_file, dest_file_path)
        ssh.close()
        os.remove(temp_file)
        return {"message": "File transferred successfully"}
    except Exception as e:
        try:
            ssh.close()
        except:
            pass
        raise RuntimeError(f"Error during SCP transfer: {str(e)}")
 
# Example usage:
if __name__ == "__main__":
    try:
        result = scp_transfer(
            source_host="source_host_ip",
            source_user="source_username",
            source_file_path="/path/to/source/file",
            dest_host="destination_host_ip",
            dest_user="destination_username",
            dest_file_path="/path/to/destination/file",
            port=22  # Example port number, adjust as needed
        )
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")