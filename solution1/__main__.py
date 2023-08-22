import os
import shutil
import glob
import csv
import datetime


class ImageMetadata():
    '''
    Collect all images of a folder and sub-folders in one folder and remove name extension.
    Then gather metadata of each and export a csv file with all data.
    '''

    def __init__(self):
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.source_path = os.path.join(self.script_path, "dairies")
        self.folder_path = os.path.join(self.script_path, "images")

    def image_gathering_func(self):
        # Create the destination folder
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        # Find all image files in the source folder and its sub-folders
        image_files = glob.glob(os.path.join(
            self.source_path, '**/*.jpg'), recursive=True)
        image_files.extend(glob.glob(os.path.join(
            self.source_path, '**/*.jpeg'), recursive=True))
        image_files.extend(glob.glob(os.path.join(
            self.source_path, '**/*.png'), recursive=True))

        # Copy each image file to the destination folder
        for image_file in image_files:
            destination_path = os.path.join(
                self.folder_path, os.path.basename(image_file))
            shutil.copy2(image_file, destination_path)

        print("Images are gathered successfully.")

    def image_metadata_exporter(self):
        # set to hold all image files
        images = set()

        # loop through all files and folders in the folder
        for root, dirs, files in os.walk(self.folder_path):
            for file in files:
                # check if the file is an image file
                if any(file.lower().endswith(ext) for ext in [".jpg", ".jpeg", ".png"]):
                    # add the file to the images set
                    images.add(os.path.join(root, file))

        # create a csv file to write image details
        with open("image_details.csv", mode="w") as file:
            writer = csv.writer(file)
            writer.writerow(["Image", "Image Size", "Image Modification data"])

            # loop through all image files and write their details to csv
            for image in images:
                # convert size to KB and round to 2 decimal places
                size = round(os.path.getsize(image) / 1024, 2)
                # get last modified time in seconds since epoch
                last_modified = os.path.getmtime(image)
                last_modified = str(datetime.datetime.fromtimestamp(
                    last_modified))  # convert to readable format
                file_name = os.path.basename(image)
                writer.writerow([file_name, size, last_modified])

        print("CSV is made!")


images = ImageMetadata()
images.image_gathering_func()
images.image_metadata_exporter()
