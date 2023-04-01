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
# Tell the browser it's an HTML page.
print('Content-Type: text/HTML')
# Blank line to indicate end of headers.
print('')

# Take form inputs
form = cgi.FieldStorage()
deck_1 = form.getfirst("file", '')

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

print("""
Fries

</body>
</html>
""")
