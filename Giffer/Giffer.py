__author__ = 'Tramel Jones'
#Create Gifs using Moviepy
from moviepy.editor import *

clip = VideoFileClip("X:/Code/Python/Giffer/thefile.mp4").subclip(50,50)

#VideoFileClip("thefile.mkv").subclip((10,07.00),(10,08.00)).resize(0.3).to_gif("Pleasework.gif")