__author__ = 'token_000'

import Tkinter as tk
import tkFileDialog as files
#tk.create()

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid()
        self.gifButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.gifButton.grid()
        self.openfile = files.askopenfilename(self, text='Quit',
            command=self.quit)
        self.openfile.grid()
        self.savefile = files.asksaveasfilename(self, text='Quit',
            command=self.quit)
        self.savefile.grid()

app = Application()
app.master.title('Make A Dank Meme')
app.mainloop()