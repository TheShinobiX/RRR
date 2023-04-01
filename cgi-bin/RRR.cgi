#!/usr/bin/env python3
import cgi
import re


# =======================================================
# ======================= Classes =======================
# =======================================================


# =======================================================
# ====================== Functions ======================
# =======================================================


# =======================================================
# ======================== Start ========================
# =======================================================
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

New World, yo!

<!--
<form action="/file-upload"
      class="dropzone"
      id="rrr-dropzone"></form>
-->

<DIV id="dropzone">
    <FORM class="dropzone needsclick" id="rrr-upload" action="/file-upload">
        <DIV class="dz-message needsclick">
            Drop files here or click to upload.
        </DIV>
    </FORM>
</DIV>

Fries
 
</body>
</html>
""")
