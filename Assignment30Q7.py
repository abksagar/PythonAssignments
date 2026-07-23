#
import time
import os
import schedule
import shutil
import datetime
import sys


def CopyFileInDirectory(SourceFilePath,Desti_Directory):



    file_name, file_ext = os.path.splitext(os.path.basename(SourceFilePath))
    now = datetime.datetime.now()
    timestamp_filename = now.strftime("%d_%m_%Y_%H_%M_%S")

    backup_filename = f"{file_name}_{timestamp_filename}{file_ext}"
    destination_path = os.path.join(Desti_Directory, backup_filename)

    shutil.copy(SourceFilePath, destination_path)


    timestamp_log = now.strftime("%d-%m-%Y %I:%M:%S %p")
    log_entry = f"Backup completed successfully at {timestamp_log}\n"

    fobj = open("backuplog.txt","a")
    fobj.write(log_entry)

    print(f"Backup created: {backup_filename}")
    print(f"Logged to 'backup_log.txt': {log_entry.strip()}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <source_file_path> <destination_directory>")
        print("Example: python script_name.py Data.txt ./BackupFolder")
        sys.exit(1)

    else:
        schedule.every(1).minute.do(CopyFileInDirectory,sys.argv[1],sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)   


if __name__ =="__main__":
    main()
