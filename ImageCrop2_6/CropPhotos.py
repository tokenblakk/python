from Crop import *
logging.info('Moving and Cropping. Origin: %s  Destination: %s', org,  dest)
moveCrop(org, dest, removeFile)
logging.info('Done.')