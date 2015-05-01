__author__ = 'Tramel Jones'
__email__ = 'tramel.jones@gmail.com'
#EDIT - Once 3 monitors are connected, create crop that splits each screen's resolution. 
#PARTIALLY DONE. 2 monitor functionality finished. 
#EDIT - Save into directory under subfolders 1/2/3.
#PARTIALLY DONE. 2 monitor functionality finished. 
#EDIT 4/20/2015 - Adding splitter functionality. 
#SPLIT.PY DONE
#2014 designed to autocrop images in my setup using Intel i7 "GLaDOS"
from PIL import Image
from config import *
import os
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s', level=logLevel, filename='debug.log')
from datetime import datetime
global ext
#Your preferred extension

logging.info('Starting up.')
#starts arbitrarily in the middle because my monitor is between two smaller ones. Change the postion of the box to suit your needs


#Depreciated - use moveCrop
# def Crop():
#     print("Cropping...")
#     for filename in os.listdir(path):
#         _thefile = path+filename
#         if _thefile.endswith(".png"):
#             #or your preferred extension
#             crop1080(_thefile)
#             #WARNING THIS DISCARDS THE SOURCE FILE
#             #IT IS SUGGESTED TO COPY IMAGES 
#             #TO THE SOURCE FOLDER IF YOU DO NOT WISH
#             #TO LOSE THE ORIGINALS
#             os.remove(_thefile)
#     print("Images cropped and backups deleted.")

def moveCrop(orgpath, dest, remove = True):
	#This is a fucking logging wrapper. 
	#The heavy lifting is done in
	#SuperMoveCrop1080 :)
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
        if _thefile.endswith(ext):
            #or your preferred extension
            SuperMoveCrop1080(_thefile, dest, 0, 0, *monitor)
            #This only crops one monitor. Try Split(TM)!
            logging.debug('Moving and cropping file %s (%d of %d)', _thefile, counter, count)
            #WARNING THIS DISCARDS THE SOURCE FILE
            #IT IS SUGGESTED TO COPY IMAGES 
            #TO THE SOURCE FOLDER IF YOU DO NOT WISH
            #TO LOSE THE ORIGINALS
            if remove:
            	os.remove(_thefile)
            #print(str(counter) + " of " + str(count) + " images cropped and moved.")
        else:
            logging.info('Skipping file %s (%d of %d)', _thefile, counter, count)
            skip += 1
    total = counter-skip
    print(str(total) + " Images cropped and moved. " + str(skip) + " files skipped")
    logging.info('%d Images cropped and moved. %d files skipped', total, skip)
    logging.info('moveCrop done.')

def SuperMoveCrop1080(name, dest, x1, y1, x2, y2):
    setTime = datetime.now()
    im = Image.open(name)
    box = (x1, y1, x2, y2)
    region = im.crop(box)
    region.save(dest + "/" + str(setTime).replace(":","_") + "_" + str(x2) + "x" + str(y2) + ext)

    #region.save(path + "/Results/" +  "_".join(map(str,setTime)) + "_768" + ext)
    #for future reference use. Intended to go with time.localtime() but it overwrites files
    #due to localtime truncating milliseconds


#DEPRECIATED USE SuperMOveCrop1080
# def moveCrop1080(name, dest):
#     setTime = datetime.now()
#     im = Image.open(name)
#     box = (0,0,1920,1080)
#     region = im.crop(box)
#     region.save(dest + "/" + str(setTime).replace(":","_") + "_1080" + ext)

    #region.save(path + "/Results/" +  "_".join(map(str,setTime)) + "_768" + ext)
    #for future reference use. Intended to go with time.localtime() but it overwrites files
    #due to localtime truncating milliseconds


#sorry for not being modular. I only call the 1080 crop function because it suits my needs. Feel free to change box dimensions to whichever configurations you need. 
if __name__ == "__main__":
	print("Cropping.")
	logging.info('Moving and Cropping. Origin: %s  Destination: %s', org,  dest)
	moveCrop(org, dest, removeFile)
	logging.info('Done.')