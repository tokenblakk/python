import subprocess as sp
import re

import numpy as np
from moviepy.conf import FFMPEG_BINARY # ffmpeg, ffmpeg.exe, etc...
from moviepy.tools import cvsecs


class FFMPEG_VideoReader:
    
    def __init__(self, filename, print_infos=False, pix_fmt="rgb24"):
        
        self.filename = filename
        self.pix_fmt = pix_fmt
        self.initialize()
        self.depth = 4 if pix_fmt=="rgba" else 3 
        self.load_infos(print_infos)
        self.pos = 1
        self.lastread = self.read_frame()
        
        
    
    def initialize(self):
        """ Opens the file, creates the pipe. """
        
        cmd = [ FFMPEG_BINARY, '-i', self.filename,
                '-f', 'image2pipe',
                "-pix_fmt", self.pix_fmt,
                '-vcodec', 'rawvideo', '-']
        self.proc = sp.Popen( cmd, stdin=sp.PIPE,
                                   stdout=sp.PIPE,
                                   stderr=sp.PIPE)
        
    
    def load_infos(self, print_infos=False):
        """ reads the FFMPEG info on the file and sets self.size
            and self.fps """
        # open the file in a pipe, provoke an error, read output
        proc = sp.Popen([FFMPEG_BINARY,"-i",self.filename, "-"],
                stdin=sp.PIPE,
                stdout=sp.PIPE,
                stderr=sp.PIPE)
        proc.stdout.readline()
        proc.terminate()
        infos = proc.stderr.read()
        if print_infos:
            # print the whole info text returned by FFMPEG
            print infos
            
        lines = infos.splitlines()
        if "No such file or directory" in lines[-1]:
            raise IOError("%s not found ! Wrong path ?"%self.filename)
        
        # get the output line that speaks about video
        line = [l for l in lines if ' Video: ' in l][0]
        
        # get the size, of the form 460x320 (w x h)
        match = re.search(" [0-9]*x[0-9]*(,| )",line)
        self.size = map(int,line[match.start():match.end()-1].split('x'))
        
        # get the frame rate
        match = re.search("( [0-9]*.| )[0-9]* (tbr|fps)",line)
        self.fps = float(line[match.start():match.end()].split(' ')[1])
        
        # get duration (in seconds)
        line = [l for l in lines if 'Duration: ' in l][0]
        match = re.search(" [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9]",line)
        hms = map(float,line[match.start()+1:match.end()].split(':'))
        self.duration = cvsecs(*hms)
        self.nframes = int(self.duration*self.fps)
    
    def close(self):
        self.proc.terminate()
        for std in self.proc.stdin,self.proc.stdout,self.proc.stderr:
            std.close()
        del self.proc
    
    def skip_frames(self,n=1):
        """ Reads and throws away n frames """
        w,h = self.size
        for i in range(n):
            self.proc.stdout.read(self.depth*w*h)
            self.proc.stdout.flush() 
        self.pos += n 
    
    
    def read_frame(self):
        w,h = self.size
        try:
            # Normally, the readr should not read after the last frame...
            # if it does, raise an error.
            s = self.proc.stdout.read(self.depth*w*h)
            result = np.fromstring(s,
                             dtype='uint8').reshape((h,w,len(s)/(w*h)))
            self.proc.stdout.flush()
        except:
            self.proc.terminate()
            serr = self.proc.stderr.read()
            print "error: string: %s, stderr: %s"%(s,serr)
            raise
            
        self.lastread = result
        
        return result
    
    
    def reinitialize(self,starttime=0):
        """ Restarts the reading, starts at an arbitrary
            location (!! SLOW !!) """
        self.close()
        if starttime==0:
            self.initialize()
        else:
            offset = min(1,starttime)
            cmd = [ FFMPEG_BINARY, '-ss',"%.03f"%(starttime- offset),
                    '-i', self.filename,
                    '-ss', "%.03f"%offset,
                    '-f', 'image2pipe',
                    "-pix_fmt", self.pix_fmt,
                    '-vcodec','rawvideo', '-']
            self.proc = sp.Popen(cmd, stdin=sp.PIPE,
                                       stdout=sp.PIPE,
                                      stderr=sp.PIPE)
                
    def get_frame(self,t):
        """ Reads a frame at time t. Note for coders:
            getting an arbitrary frame in the video with ffmpeg can be
            painfully slow if some decoding has to be done. This
            function tries to avoid fectching arbitrary frames whenever
            possible, by moving between adjacent frames.
            """
        if t<0:
            t=0
        elif t>self.duration:
            t = self.duration
            
        pos = int(self.fps*t)+1
        if pos == self.pos:
            return self.lastread
        else:
            if (pos < self.pos) or (pos> self.pos+100):
                self.reinitialize(t)  
            else:
                self.skip_frames(pos-self.pos-1)
            result =  self.read_frame()
            self.pos = pos
            return result
            

def read_image(filename,with_mask=True):
    pix_fmt='rgba' if with_mask else "rgb24"
    vf = FFMPEG_VideoReader(filename, pix_fmt=pix_fmt)
    vf.close()
    return vf.lastread
