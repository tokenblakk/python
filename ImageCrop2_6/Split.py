__author__ = "Tramel Jones"
__email__ = 'tramel.jones@gmail.com'
#2015 designed to autocrop images in my setup using Intel i7 "GLaDOS"
#Define monitors in config.py and add to monitors list before running Split.py
from Crop import *

if  not os.path.exists(dest):
    os.mkdir(dest)
if  not os.path.exists(org):
    os.mkdir(org)
if  not os.path.exists(dest + "/2"):
    os.mkdir(dest + "/2")

def Split(orgpath, dest, remove = True):
    print("Splitting.")
    logging.info('SuperSplit started.')
    counter = 0
    skip = 0
    count = len(os.listdir(orgpath))
    for filename in os.listdir(orgpath):
        counter += 1
        os.system('cls')
        _thefile = orgpath + filename
        print(str(counter) + " of " + str(count))
        print("Stretching apart seams. File destination: " + dest)
        if _thefile.endswith(".png"):
            #or your preferred extension  
            xpos = 0
            for index, monitor in enumerate(monitors):
                print("Monitor " + str(index+1) + ": " + str(monitor[0]) + "x" + str(monitor[1]))
            for index, monitor in enumerate(monitors):
                if  not os.path.exists(dest + "/" + str(index+1)):
                    os.mkdir(dest + "/" + str(index+1))
                SuperMoveCrop1080(_thefile, dest + "/" + str(index+1), xpos, 0, xpos + monitor[0], monitor[1])
                xpos += monitor[0]
            logging.debug('Moving and cropping file %s (%d of %d)', _thefile, counter, count)
            #WARNING THIS DISCARDS THE SOURCE FILE
            #IT IS SUGGESTED TO COPY IMAGES 
            #TO THE SOURCE FOLDER IF YOU DO NOT WISH
            #TO LOSE THE ORIGINALS
            if remove:
                os.remove(_thefile)
        else:
            logging.info('Skipping file %s (%d of %d)', _thefile, counter, count)
            skip += 1
    total = counter-skip
    print(str(total) + " Images cropped and moved. " + str(skip) + " files skipped")
    logging.info('%d Images cropped and moved. %d files skipped', total, skip)
    logging.info('Split done.')

if __name__ == "__main__":
    logging.info('Splitting. Origin: %s  Destination: %s', org,  dest)
    Split(org, dest, removeFile)
    logging.info('Done.')