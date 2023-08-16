# Project CleanUp

## Description
Project CleanUp is a set of Python scripts designed to organize and clean up files and directories on your computer. It includes three scripts:

1. `add_to_folds.py`: This script organizes files in the Downloads directory into specific folders based on their file types. It creates folders for different file types such as Images, Code, Documents, Audio, Video, Photoshop files, and Applications. Files are moved to their respective folders based on their file extensions.

2. `del_temp.py`: This script deletes temporary files and directories from specified locations on your computer. It removes files with extensions like .log, .cache, .tmp, .dmg, and .pkg from directories such as /private/var/folders, ~/Library/C
aches, ~/Library/Logs, ~/Downloads, and ~/Desktop. Additionally, it deletes screenshot files starting with "Screenshot" from the ~/OneDrive/Desktop directory.

3. `del_duplicates.py`: This script removes duplicate files from a specified directory. It identifies duplicate files by comparing their names and numbers in parentheses. The script keeps the latest version of the file and removes the rest. It 
also renames the latest file to remove the number in parentheses.

## Usage
1. Run `add_to_folds.py` to organize files in the Downloads directory. It will create folders for different file types and move files to their respective folders based on their extensions.
                                                                                                                                                                                            
2. Run `del_temp.py` to delete temporary files and directories from specified locations on your computer. It will remove files with specific extensions and screenshot files from the specified directories.
                                                                                                                                                                                                            
3. Run `del_duplicates.py` to remove duplicate files from a specified directory. It will keep the latest version of each file and remove the rest. It will also rename the latest file to remove the number in parentheses.
                                                                                                                                                                                                                           
## Requirements                                                                                                                                                                                                            
- Python 3.x
- Operating System:  Windows (scripts were tested and developed on windows)

## Note
- Please use these scripts with caution as they perform file operations that cannot be undone. Make sure to backup important files before running these scripts.
- Modify the file paths and directories in the scripts according to your specific needs before running them.
- These scripts are provided as-is and the developer is not responsible for any data loss or damage caused by their usage.


