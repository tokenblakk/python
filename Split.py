from Crop import *

if  not os.path.exists(dest + "/1"):
    os.mkdir(dest + "/1")
if  not os.path.exists(dest + "/2"):
    os.mkdir(dest + "/2")

def Split(orgpath, dest, remove = True):
    print("Splitting.")
    logging.info('SuperSplit started.')
    counter = 0
    skip = 0
    monitors = 2
    count = len(os.listdir(orgpath))
    for filename in os.listdir(orgpath):
        counter += 1
        os.system('cls')
        _thefile = orgpath + filename
        print(str(counter) + " of " + str(count))
        print("Stretching apart seams. File destination: " + dest)
        if _thefile.endswith(".png"):
            #or your preferred extension  
            print("Monitor1: " + str(monitor1) + " Monitor2: " + str(monitor2))
            SuperMoveCrop1080(_thefile, dest + "/1", 0, 0, *monitor1)
            SuperMoveCrop1080(_thefile, dest + "/2", monitor1[0], 0, monitor1[0]+monitor2[0], monitor2[1])
            #moveCrop1080(_thefile, dest)
            # Add another monitor

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
    logging.info('Split done.')

logging.info('Splitting. Origin: %s  Destination: %s', org,  dest)
Split(org, dest, removeFile)
logging.info('Done.')