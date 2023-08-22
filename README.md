# et3-egypt-exercise

## Problem 1 (Image Metadata Extractor)
Given a dataset of Images splitted into folders, extract all images from folders and sub-folders and copy them to a single folder “called: images”

Note: There is no specific depth of sub-folders.
- For each image name in images_dataset, there is a prefix which should be discarded. (for ex: jdwjs-image1.jpg becomes image1.jpg).
- For each image in images_dataset, extract image name and size and the date of last image content modification.

Modification examples: crop images or change its orientation.

➢ Input: Dataset of Images

➢ Output:
- extracted images to one folder
- A csv file (report) that specify the following:
    - image name “with the prefix discarded.”
    - image size
    - image last modification date

### Usage Guide

#### Requird Packages
- Python3

#### Run Script
1. Clone git repo
```shell
git clone https://github.com/mahmoudk1000/et3-egypt-exercise.git
```
2. Change working directory
```shell
cd et3-egypt-exercise/solution1
```
3. Run Script
```python
python3 __main__.py
```

---

## Problem 2 (Object Detector)
Give an image, filled with objects (products). It will extracts and detect all content of the image. Then save corespoding data into a text file. and later convert it into JSON format.

### Usage Guide

#### Requird Packages
- Python3
- [cv2](https://opencv.org/) library

#### Run Script
1. Clone git repo
```shell
git clone https://github.com/mahmoudk1000/et3-egypt-exercise.git
```
2. Change working directory
```shell
cd et3-egypt-exercise/solution2
```
3. Run Script
```python
python3 __main__.py
```
