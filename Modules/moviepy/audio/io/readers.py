import subprocess as sp
import re
import time
import os

import numpy as np

#from moviepy.clip import Clip
from moviepy.tools import cvsecs
from moviepy.video.io.preview import imdisplay
from moviepy.conf import FFMPEG_BINARY
from moviepy.tools import cvsecs



    
class FFMPEG_AudioReader:
    """ streams any file (audio or video) and outputs a 16bit 44100HZ
        wav that can be read by the moviepy AudioFileClip. """
        
    def __init__(self, filename, print_infos=False, fps=44100, nbytes=2):
        self.filename = filename
        self.nbytes = nbytes
        self.fps = fps
        self.f = 's%dle'%(8*nbytes)
        self.acodec = 'pcm_s%dle'%(8*nbytes)
        self.nchannels = 2
        self.load_infos()
        self.initialize()
       
        
        
    
    def initialize(self):
        """ Opens the file, creates the pipe. """
        
        cmd = [  FFMPEG_BINARY, '-i', self.filename, '-vn',
               '-f', self.f,
               '-acodec', self.acodec,
               '-ar', "%d"%self.fps,
               '-ac', '%d'%self.nchannels, '-']
        self.proc = sp.Popen( cmd, stdin=sp.PIPE,
                                   stdout=sp.PIPE,
                                   stderr=sp.PIPE)
        self.pos = 1
    
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
            
        # get duration (in seconds)
        line = [l for l in lines if 'Duration: ' in l][0]
        match = re.search(" [0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9]",line)
        hms = map(float,line[match.start()+1:match.end()].split(':'))
        self.duration = cvsecs(*hms)
        self.nframes = int(self.duration*self.fps)
    
    
    def reinitialize(self,starttime=0):
        """ Restarts the reading, starts at an arbitrary
            location (!! SLOW !!) """
        self.close()
        if starttime==0:
            self.initialize()
        else:
            offset = min(1,starttime)
            cmd = [ FFMPEG_BINARY,
                    "-ss", "%.05f"%(starttime-offset),
                    '-i', self.filename, '-vn',
                    "-ss", "%.05f"%offset,
                    '-f', self.f,
                    '-acodec', self.acodec,
                    '-ar', "%d"%self.fps,
                    '-ac', '%d'%self.nchannels, '-']
            self.proc = sp.Popen(cmd, stdin=sp.PIPE,
                                       stdout=sp.PIPE,
                                      stderr=sp.PIPE)
            self.pos = int(self.fps*starttime)+1
     
    def skip_chunk(self,chunksize):
        s = self.proc.stdout.read(self.nchannels*chunksize*self.nbytes)
        self.proc.stdout.flush()
        self.pos = self.pos+chunksize
        
    def read_chunk(self,chunksize):
        s = self.proc.stdout.read(self.nchannels*chunksize*self.nbytes)
        dt = {1: 'int8',2:'int16',4:'int32'}[self.nbytes]
        result = np.fromstring(s, dtype=dt)
        result = (1.0*result / 2**(8*self.nbytes-1)).\
                                 reshape((len(result)/self.nchannels,
                                          self.nchannels))
        self.proc.stdout.flush()
        self.pos = self.pos+chunksize
        return result
                    
    def seek(self,pos):
        """ Reads a frame at time t. Note for coders:
            getting an arbitrary frame in the video with ffmpeg can be
            painfully slow if some decoding has to be done. This
            function tries to avoid fectching arbitrary frames whenever
            possible, by moving between adjacent frames.
            """
        if (pos < self.pos) or (pos> (self.pos+1000000)):
            t = 1.0*pos/self.fps
            self.reinitialize(t)  
        elif pos > self.pos:
            self.skip_chunk(pos-self.pos)
        self.pos = pos
    
    def close(self):
        self.proc.terminate()
        for std in self.proc.stdin,self.proc.stdout,self.proc.stderr:
            std.close()
        del self.proc
        
        
        
        
        
class WaveReader:
    
    def __init__(self, filename):
        if not filename.endswith('.wav'):
            name, ext = os.path.splitext(os.path.basename(filename))
            if temp_wav is None:
                filename = Clip._TEMP_FILES_PREFIX + filename+'.wav'
            if not os.exists(filename):
                ffmpeg.extract_sound(filename, temp, fps, bitrate)
                
        self.filename = filename

        wavf = wave.open(filename)
        self.nchannels = wavf.getnchannels()
        self.fps = wavf.getframerate()
        self.nframes = wavf.getnframes()
        self.nbytes = wavf.getsampwidth()
        self._wavfile = wavf
        
        self.duration = (1.0*self.nframes/self.fps)
        self.end = self.duration
        self.np_dtype = {1:'int8',2:'int16',4:'int32'}[self.nbytes]
        
        self.buffersize= buffersize
        self._buffer_around(0)
