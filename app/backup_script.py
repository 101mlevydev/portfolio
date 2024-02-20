import os
import shutil
import time

UTIL_NAME = "backup_util"
BACKUP_DIR ="/backup"
CONFIG_FILE = "/opt/backup_util/backup_util.conf"

def check_backup_directory():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

def read_conf_file():
    files_to_backup = ["/etc/hosts", "/etc/resolve.conf"]
    with open(CONFIG_FILE, "r") as config_file:
        for line in config_file:
            file_path = line.strip()
            if os.path.exists(file_path):
                file_to_backup.append(file_path)
            else:
                print(f"file '(file_path)' does not exist. moving to the next file")
                return files_to_backup 

def backup():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    for source_file in SOURCE_FILES:
        try:
            filename = os.path.basename(source_file)
            destination = os.path.join(BACKUP_DIR, f"(filename)_(timestamp)")
            shutil.copy(source_file, destination)
        except Exception as e:
            print(f"warning: Backup of (source_file) failed. {str(e)}")
            with open(os.path.join(BACKUP_DIR, "failure.log"), "a") as log_file:
                log_file.write(f"{time.ctime()}: Backup of (source_file) failed. Reason: {str(e)}\n")

def main():
    check_backup_directory()
    files_to_backup = read_backup_config()
    while True:
        backup(files_to_backup)
        time.sleep(3600)

if __name__ = "__main__":
    main()
