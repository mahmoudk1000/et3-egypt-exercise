import cv2
import json

# Load the image
img = cv2.imread('image.jpg')

# Define the object detection algorithm to be used
object_detection_algorithm = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Apply the object detection algorithm to detect objects in the image
objects = object_detection_algorithm.detectMultiScale(img)

# Write the detected objects' coordinates and dimensions to a text file
with open('output.txt', 'w') as f:
    for i, (x, y, w, h) in enumerate(objects):
        f.write(f'Object {i+1}: x={x}, y={y}, width={w}, height={h}\n')

# Convert the text file to json format
data = {}
with open('output.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split(': ')
        data[key] = value

json_data = json.dumps(data)

# Write the json data to a file
with open('output.json', 'w') as f:
    f.write(json_data)