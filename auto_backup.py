from datetime import date
from shutil import copy
import os

date_backup = date.today()
print(date_backup)

str_date_backup = str(date_backup).replace('-','.')
print(str_date_backup)

# path_input = r'/Users/robindias/Files/Robin Dias - Blue.docx'
path_input = input(r'Please specify the path of the file to be backed up?')
file_name = os.path.basename(path_input)
path_output = r'/Users/robindias/Backup_files/' + '\\' + str_date_backup + ' - ' + file_name
print(path_output)

copy(path_input,path_output)
print("File was successfully saved")