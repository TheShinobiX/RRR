#!/usr/bin/env python3
import cgi
import re
import os
import cgitb
cgitb.enable()

# =======================================================
# ======================= Classes =======================
# =======================================================


# =======================================================
# ====================== Functions ======================
# =======================================================


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

print("""
Fries

</body>
</html>
""")
