import io
import os
import tkinter as tk
from tkinter import filedialog
import sys
import cv2
from difflib import get_close_matches
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# =======================================================
# ======================= Classes =======================
# =======================================================


# =======================================================
# ====================== Functions ======================
# =======================================================
def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    labels = []
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        labels.append(object_.name)
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
    return labels


def localize_objects_uri(uri):
    """Localize objects in the image on Google Cloud Storage

    Args:
    uri: The path to the file in Google Cloud Storage (gs://...)
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    image = vision.Image()
    image.source.image_uri = uri

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))


# =======================================================
# ======================== Start ========================
# =======================================================
# Read dataset into dictionary
compost_dict = {}
key_list = []
with open("compost_dataset.txt") as f:
    for line in f:
        key_flag = True
        buffer_key = ""
        buffer_val = ""
        for char in line:
            if key_flag:
                if char != ":":
                    buffer_key += char
                else:
                    key_flag = False
            else:
                buffer_val += char
        new_key = buffer_key[:-1]
        new_val = buffer_val[1:].replace('\n', '')
        compost_dict[new_key] = new_val
        key_list.append(new_key)

print("Dataset Length: {}".format(len(compost_dict)))
key_list_len = len(key_list)
print("Keys: {}\n".format(key_list_len))

# Get user image
print("Select File")
root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()
if filename == "":
    print("--- Cancelled ---")
    sys.exit(0)
print("Loaded from {} successfully".format(filename))

# Perform object recognition
labels = localize_objects(filename)

print()
print("=== === === Results === === ===")

# Check if each object is compostable
for obj in labels:
    # get close objects in our keys if there
    str_matches = get_close_matches(obj, key_list, key_list_len, 0.53)
    if str_matches:
        # if any of the matches are a yes or maybe
        yes_flag = False
        maybe_flag = False
        for str_match in str_matches:
            compostable_val = compost_dict.get(str_match, None)
            if compostable_val == "yes":
                yes_flag = True
                break
            elif compostable_val == "maybe":
                maybe_flag = True
        if yes_flag:
            print("{}: YES, compost-able".format(obj))
        elif maybe_flag:
            print("{}: MAYBE, careful of bacteria or amount".format(obj))
        else:
            print("{}: NO, please no! do NOTTT compost this".format(obj))
    else:
        print("{}: NO, please no! do NOTTT compost this".format(obj))

# Display image for reference
img = mpimg.imread(filename)
plt.imshow(img)
plt.show()
