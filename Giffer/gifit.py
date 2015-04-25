__author__ = 'tjones'

from moviepy.editor import *

def time_symetrize(clip):
    """ Returns the clip played forwards then backwards. In case
    you are wondering, vfx (short for Video FX) is loaded by
    >>> from moviepy.editor import * """
    return concatenate([clip, clip.fx( vfx.time_mirror )])



#clip.preview()

def dankmeme(filein, fileout, start, stop, resize=0.8, reverse=True):
    if filein and fileout:
        print 'filein: '
        print filein
        print 'fileout: '
        print fileout
        print 'start: '
        print start
        print 'stop: '
        print stop
        print 'reverse'
        print reverse
        print 'resize'
        print resize

        if reverse:
            clip = (VideoFileClip(filein)
                    .subclip(start, stop)
                    #.subclip((2,19.0),(2,21.0))
                    .resize(resize)
                    #.crop(x1=720, x2=1000)
                    .fx(time_symetrize)
                    )
        else:
            clip = (VideoFileClip(filein)
                    .subclip(start, stop)
                    .resize(resize)
                    )
        """
        text = (TextClip("Looking good\nTramel.",
                         fontsize=30, color='white',
                         font='Amiri-Bold', interline=5)
                .set_pos((260, 90))
                .set_duration(clip.duration))
        """
        #composition = CompositeVideoClip([clip, text])
        #composition.preview()
        clip.write_gif(fileout)
        #composition.write_gif(fileout)