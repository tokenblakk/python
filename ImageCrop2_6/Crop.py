__author__ = 'Tramel Jones'
#2014 designed to autocrop images in my setup using Intel i7 "GLaDOS"
from PIL import Image
import os
from datetime import datetime
global ext
#Your preferred extension
ext = ".png"
#your path for source folder
path = "X:/Photos/Crop/"

#starts arbitrarily in the middle because my monitor is between two smaller ones. Change the postion of the box to suit your needs
def crop1080(name):
    setTime = datetime.now()
    im = Image.open(name)
    box = (1280,0,3200,1080)
    region = im.crop(box)
    region.save(path + "Results/" + str(setTime).replace(":","_") + "_1080" + ext)

def crop1080Dual(name):
    setTime = datetime.now()
    im = Image.open(name)
    box = (0,0,1920,1080)
    region = im.crop(box)
    region.save(path + "Results/" + str(setTime).replace(":","_") + "_1080" + ext)

def crop768Triple(name):
    setTime = datetime.now()
    im = Image.open(name)
    box = (3200,74,4560,842)
    region = im.crop(box)
    region.save(path + "Results/" + str(setTime).replace(":","_") + "_768" + ext)

def crop768Dual(name):
    setTime = datetime.now()
    im = Image.open(name)
    box = (1176,0,2536,768)
    region = im.crop(box)
    region.save(path + "Results/" + str(setTime).replace(":","_") + "_768" + ext)
    #region.save(path + "/Results/" +  "_".join(map(str,setTime)) + "_768" + ext)
    #for future reference use. Intended to go with time.localtime() but it overwrites files
    #due to localtime truncating milliseconds

def crop718(name):
    setTime = datetime.now()
    im = Image.open(name)
    box = (0,330,1280,1048)
    region = im.crop(box)
    region.save(path + "Results/" + str(setTime).replace(":","_") + "_718" + ext)

#sorry for not being modular. I only call the 1080 crop function because it suits my needs. Feel free to change line 50 to whichever function you need
print("Cropping...")
for filename in os.listdir(path):
    _thefile = path+filename
    if _thefile.endswith(".png"):
        #or your prefferred extension
        crop1080(_thefile)
        #WARNING THIS DISCARDS THE SOURCE FILE IT IS SUGGESTED TO COPY IMAGES TO THE SOURCE FOLDER IF YOU DO NOT WISH TO LOSE THE ORIGINALS
        os.remove(_thefile)
print("Images cropped and backups deleted.")
