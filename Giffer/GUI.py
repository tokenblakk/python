__author__ = 'tjones'

import Tkinter as tk
import tkMessageBox
import tkFileDialog as files
import Tkconstants as constants
from gifit import *


class GifGUI(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        #vars
        self.openfile = tk.StringVar()
        self.saveas = tk.StringVar()
        self.is_reversed = tk.BooleanVar()

        #button options
        button_opt = {'fill': constants.BOTH, 'padx': 5, 'pady': 5}

        #buttons
        tk.Button(self, text='Select video file', command=self.askopenfilename).pack(**button_opt)
        tk.Label(self, textvariable=self.openfile).pack()
        tk.Button(self, text='Save .gif as...', command=self.asksaveasfilename).pack(**button_opt)
        tk.Label(self, textvariable=self.saveas).pack()

        tk.Label(self, text='Start time: 00:00:00.0').pack()
        self.starttime = tk.Entry(self)
        self.starttime.pack()
        self.starttime.insert(0, '00:00:00.0')

        tk.Label(self, text='Stop time: 00:00:00.0').pack()
        self.stoptime = tk.Entry(self)
        self.stoptime.pack()
        self.stoptime.insert(0, '00:00:00.0')

        tk.Label(self, text='Resize amount').pack()
        self.resize = tk.Entry(self)
        self.resize.pack()
        self.resize.insert(0, '0.8')

        tk.Label(self, text='Reverse Loop?').pack()
        self.reverse = tk.Checkbutton(self, variable=self.is_reversed)
        self.reverse.pack()



        tk.Button(self, text='START!', command=self.calldankmeme).pack()
        tk.Button(self, text='Close', command=self.quit).pack()


        self.openfile_opt = options = {}
        options['defaultextension'] = '.mp4'
        options['filetypes'] = [('.mp4 files', '.mp4'), ('.mpeg files', '.mpeg'), ('.avi files', '.avi'), ('.mkv files', '.mkv')]
        options['initialdir'] = 'C:\\'
        options['parent'] = root
        options['title'] = 'Open a Dank Meme'

        self.savefile_opt = options = {}
        options['defaultextension'] = '.gif'
        options['filetypes'] = [('.gif files', '.gif')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'dankmeme.gif'
        options['parent'] = root
        options['title'] = 'Save a Dank Meme'

    def askopenfilename(self):
        """
        :return: filename to open
        """
        self.openfile.set(files.askopenfilename(**self.openfile_opt))
        return self.openfile.get()

    def asksaveasfilename(self):
        """
        :return: filename to save as
        """
        self.saveas.set(files.asksaveasfilename(**self.savefile_opt))
        return self.saveas.get()
    def calldankmeme(self):
        if self.openfile.get() and self.saveas.get():
            tkMessageBox.showinfo("Loading memes", "Please wait...")
            dankmeme(self.openfile.get(), self.saveas.get(), self.starttime.get(), self.stoptime.get(),
                     #0.8,
                     float(self.resize.get()),
                     self.is_reversed.get())
            tkMessageBox.showinfo("Dank Ass Meme", "You made a .gif!")


if __name__ =='__main__':
    root = tk.Tk()
    GifGUI(root).pack()
    root.title('Dank Meme Generator')
    root.iconbitmap('favicon.ico')
    root.mainloop()