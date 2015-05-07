import logging
#logLevel = logging.DEBUG
logLevel = logging.INFO
ext = ".png"
#org: your path for source folder 
#dest: your destination folder
#org = "X:/Dropbox/test/"
#dest = "X:/Photos/Crop/Results/test"
org = "X:/Dropbox/Screenshots/"
dest = "X:/Photos/Crop/Results/"

#Switch on or off to remove source file after crop.
#Useful for debugging
#or saving precious memories
removeFile = True

#monitor: for use with Crop.py
monitor = [1920, 1080]

#monitors: for use with Split.py
#define new monitor here
#and append to monitors list 
#for as many monitors as you'd like.
monitor1 = [1360, 768]
monitor2 = [1920, 1080]
monitor3 = [1360, 768]
monitors = (monitor1, monitor2, monitor3)