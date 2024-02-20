import os
import shutil
import time

UTIL_NAME = "backup_util"
BACKUP_DIR = "/backup"
CONFIG_FILE = "/opt/backup_util/backup_util.conf"

def check_backup_directory():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

def read_conf_file():
    files_to_backup = ["/etc/hosts", "/etc/resolv.conf"]
    with open(CONFIG_FILE, "r") as config_file:
        for line in config_file:
            file_path = line.strip()  # Remove newline characters
            if os.path.exists(file_path):
                files_to_backup.append(file_path)
            else:
                print(f"File '{file_path}' does not exist. Moving to the next file.")
    return files_to_backup  # Return the updated list of files to backup

def backup():
    timestamp = time.strftime("%Y|%m|%d|%H|%M|%S")
    files_to_backup = read_conf_file()  # Call read_conf_file inside backup() to get updated file list
    for source_file in files_to_backup:  # Iterate over files_to_backup list
        try:
            filename = os.path.basename(source_file)
            destination = os.path.join(BACKUP_DIR, f"{filename}_{timestamp}")  # Corrected the string formatting
            shutil.copy(source_file, destination)
        except Exception as e:
            print(f"Warning: Backup of {source_file} failed. {str(e)}")
            with open(os.path.join(BACKUP_DIR, "failure.log"), "a") as log_file:
                log_file.write(f"{time.ctime()}: Backup of {source_file} failed. Reason: {str(e)}\n")

def main():
    check_backup_directory()
    while True:
        backup()
        time.sleep(3600)

if __name__ == "__main__":
    main()

