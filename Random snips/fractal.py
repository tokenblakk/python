from Tkinter import*
import random 
import time



def idle5(dummy):
    '''freeze action for 5 seconds'''
    print "freeze"
    root.title("Idle, 5 seconds")
    time.sleep(5)
    root.title("Happy Circles.....")

#make window
root = Tk()
#window title
root.title("DEM FRACTALS")
print "Hello."
#width and height
w = 640
h = 480
#canvas to draw on
cv = Canvas(width = w, height = h, bd=0, highlightthickness=0, bg='black')
cv.pack()
#list colors to play with
colorList = ["blue", "red", "green", "white", "yellow", "magenta", "orange"]
#endless color loop to draw circles


#start the main loop
print "begin loop"
root.mainloop()

while 1:
    #random centre of circle (x,y) and radius r
    x = random.randint(0, w)
    y = random.randint(0, h)
    r = random.randint(5, 50)
    #choose a color
    color = random.choice(colorList)
    #draw the circle
    cv.create_oval(20, 330, 20+5, 330+5, fill ="red")
    #cv.create_oval(x, y, x+r, y+r, fill ="red")
    #update the window
    root.update
    #bind left click to calling idle
    cv.bind('<Button-1>', idle5)


