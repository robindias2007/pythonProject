from zipfile import ZipFile
import os

# Zip single file
# zip_file = zipfile.ZipFile('temp.zip','w')
# zip_file.write('Robin_Devops Resume (1) (1).pdf', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.close()

def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root,directories,files in os.walk(directory):
        for filename in files:
        # join the two strings in order to form the full filepath.
            filepath = os.path.join(root,filename)
            file_paths.append(filepath)

        #returning all filepaths
        return file_paths

def main():
    # path to folder which needs to be zipped
    #directory = r'/Users/robindias/Downloads/personal documents'
    directory = input(r'Please specify the location you want to zip?')

    # calling function to get all file paths in the directory
    file_paths = get_all_file_paths(directory)

    #name of the zip directory
    zip_name = os.path.basename(directory)

    # printing the list of all files to be zipped
    print("Print the list of all files to be zipped")
    for filename in file_paths:
        print(filename)


    #writing files to a zipfile
    with ZipFile(zip_name + '.zip','w') as zip:
        #writing each file one by one
        for file in file_paths:
            zip.write(file)

    print("All Files zipped successfully")

#To call the function
if __name__ == "__main__":
    main()




