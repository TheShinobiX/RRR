#!/usr/bin/env python3
import cgi
import re
import os
import io
import cgitb
cgitb.enable()
# from google.cloud import vision

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
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))


def localize_objects_uri(uri):
    """Localize objects in the image on Google Cloud Storage

    Args:
    uri: The path to the file in Google Cloud Storage (gs://...)
    """

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
# Tell the browser it's an HTML page.
print('Content-Type: text/HTML')
# Blank line to indicate end of headers.
print('')

# Take form data
form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form["file"]
fn = None
content = ""
if fileitem.file:
    # yay...we got a file
    fn = os.path.basename(fileitem.filename)
    # Save the file
    content = fileitem.file.read()
    with open("../RRR_dir/{}".format(fn), "wb") as f:
        f.write(content)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tandoori</title>
    <script src="https://unpkg.com/dropzone@5/dist/min/dropzone.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/dropzone@5/dist/min/dropzone.min.css" type="text/css" />
    <script src="../RRR.js"></script>
    <link rel="stylesheet" href="../RRR.css" type="text/css" />
</head>
<body>
""")

if fn:
    print("""<img src="../RRR_dir/{}" alt="User input image">""".format(fn))

# localize_objects_uri("https://cloud.google.com/vision/docs/images/bicycle_example.png")

print("""

</body>
</html>
""")
