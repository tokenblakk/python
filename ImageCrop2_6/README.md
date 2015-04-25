*ImageCrop2_6*
============

A tool I created to crop my screenshots down to 1920x1080.
Set monitor configuration in config.py. 
Supports up to 2 monitors with Split.py
Supports 1 monitor with Crop.py. call CropPhotos.py for single monitor

WARNING: This program removes the source image, if you intend to save the originals, it is
recommended you copy images to the source folder.

*This Setting is configurable in config.py*

This program requires a source folder specified For me it is X:/Photos/Crop. Set this folder in config.py
The processed images will be placed in a new folder called /Results in your source folder.


This program uses Pillow, a fork of PIL

Available here:
https://github.com/python-imaging/Pillow

Extract "PIL/" into your C:/Python26/Lib/site-packages/ folder  (For windows, other operating systems may vary)
Happy Cropping/Splitting.
