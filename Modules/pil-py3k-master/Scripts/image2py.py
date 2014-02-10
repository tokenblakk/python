#
# The Python Imaging Library
# $Id: image2py.py 2134 2004-10-06 08:55:20Z fredrik $
#
# convert an image to a Python module
#
# to use the module, import it and access the "IMAGE" variable
#
#       import img1
#       im = img1.IMAGE
#
# the variable name can be changed with the -n option
#
# note that the application using this module must include JPEG
# and/or ZIP decoders, unless the -u option is used.
#
# Copyright (c) Secret Labs AB 1997.  All rights reserved.
# Copyright (c) Fredrik Lundh 1997.
#
# See the README file for information on usage and redistribution.
#

import Image
import getopt, io, sys

octdigits = "01234567"

def usage():
    print("image2py 0.1/97-01-03 -- convert image to python module")
    print()
    print("Usage: image2py [options] imagefile pyfile")
    print()
    print("Options:")
    print("  -n <name>    set variable name (default is 'IMAGE')")
    print("  -l           use lossy compression (JPEG) if suitable")
    print("  -u           disable compression")
    print()
    print("Provided you use distinct variable names, the output")
    print("files can be concatenated into one large module file.")
    sys.exit(1)

try:
    opt, argv = getopt.getopt(sys.argv[1:], "n:lu")
except getopt.error as v:
    usage()

name = "IMAGE"
lossy = 0
compress = 1

for o, a in opt:
    if o == "-n":
        name = a
    elif o == "-l":
        lossy = 1
    elif o == "-u":
        compress = 0

if len(argv) != 2:
    usage()

# --------------------------------------------------------------------
# convert image to string

im = Image.open(argv[0])

if im.format == "JPEG" and compress:

    # store as is
    data = open(argv[0], "rb").read()

else:

    # load and store as PNG
    fp = io.BytesIO()

    if compress:
        if lossy and im.mode in ["L", "RGB"]:
            im.save(fp, "JPEG")
        else:
            im.convert("RGB").save(fp, "PNG")
    else:
        im.save(fp, "PPM") # FIXME: won't work with "P" images

    data = fp.getvalue()

# --------------------------------------------------------------------
# convert string to python module (this is not very fast...)

fp = open(argv[1], "w")

data = repr(data)

fp.write("# generated by image2py %s\n" % argv[0])
fp.write("from io import BytesIO\n")
fp.write("import Image\n")

word = "%s = Image.open(BytesIO(b" % name

fp.write(word)
c = len(word)

i = 1
while i < len(data)-1:
    if data[i] != "\\":
        word = data[i]
        i = i + 1
    else:
        if data[i+1] in octdigits:
            for n in range(2, 5):
                if data[i+n] not in octdigits:
                    break
            word = data[i:i+n]
            i = i + n
        else:
            word = data[i:i+2]
            i = i + 2
    l = len(word)
    if c + l >= 78-1:
        # fp.write("'\n'")
        fp.write("\\\n")
        c = 0
    fp.write(word)
    c = c + l

fp.write("'))\n")