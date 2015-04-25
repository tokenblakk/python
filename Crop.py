__author__ = 'Tramel Jones'
#2014 designed to autocrop images in my setup using Intel i7 "GLaDOS"
from PIL import Image
import os
import logging
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s', level=logging.DEBUG, filename='debug.log')
from datetime import datetime
global ext
#Your preferred extension
logging.info('Starting up.')
ext = ".png"
#your path for source folder
path = "X:/Photos/Crop/"
org = "X:/Dropbox/Screenshots/"
#org = "X:/Dropbox/test/"
dest = "X:/Photos/Crop/Results"
#starts arbitrarily in the middle because my monitor is between two smaller ones. Change the postion of the box to suit your needs

def Crop():
    print("Cropping...")
    for filename in os.listdir(path):
        _thefile = path+filename
        if _thefile.endswith(".png"):
            #or your preferred extension
            crop1080(_thefile)
            #WARNING THIS DISCARDS THE SOURCE FILE IT IS SUGGESTED TO COPY IMAGES TO THE SOURCE FOLDER IF YOU DO NOT WISH TO LOSE THE ORIGINALS
            os.remove(_thefile)
    print("Images cropped and backups deleted.")

def moveCrop(orgpath, dest):
    logging.info('moveCrop started.')
    counter = 0
    skip = 0
    count = len(os.listdir(orgpath))
    for filename in os.listdir(orgpath):
        counter += 1
        os.system('cls')
        _thefile = orgpath + filename
        print(str(counter) + " of " + str(count))
        print("Moving, and Cropping. File destination: " + dest)
        if _thefile.endswith(".png"):
            #or your preferred extension
            moveCrop1080(_thefile, dest)
            logging.debug('Moving and cropping file %s (%d of %d)', _thefile, counter, count)
            #WARNING THIS DISCARDS THE SOURCE FILE IT IS SUGGESTED TO COPY IMAGES TO THE SOURCE FOLDER IF YOU DO NOT WISH TO LOSE THE ORIGINALS
            os.remove(_thefile)
            #print(str(counter) + " of " + str(count) + " images cropped and moved.")
        else:
            logging.info('Skipping file %s (%d of %d)', _thefile, counter, count)
            skip += 1
    total = counter-skip
    print(str(total) + " Images cropped and moved. " + str(skip) + " files skipped")
    logging.info('%d Images cropped and moved. %d files skipped', total, skip)
    logging.info('moveCrop done.')

def moveCrop1080(name, dest):
    setTime = datetime.now()
    im = Image.open(name)
    box = (1280,0,3200,1080)
    region = im.crop(box)
    region.save(dest + "/" + str(setTime).replace(":","_") + "_1080" + ext)

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

#sorry for not being modular. I only call the 1080 crop function because it suits my needs. Feel free to change box dimensions to whichever configurations you need. 
logging.info('Moving and Cropping. Origin: %s  Destination: %s', org,  dest)
moveCrop(org, dest)
logging.info('Done.')