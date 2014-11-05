#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)

       	   # right button
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.right = Button(self.myContainer1)
            self.right.configure(text="Right", background= "green")
            self.right.grid(row=0,column=1)	
           # left button
            self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
            self.left = Button(self.myContainer1)
            self.left.configure(text="Left", background= "green")
            self.left.grid(row=0,column=2)	
       	    self.right.bind("<Button-1>", self.rightClicked)
            self.left.bind("<Button-1>", self.leftClicked)		
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	def leftClicked(self, event):  
            global oval
            global player
            drawpad.move(player, -20, 0)   	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
        
        def rightClicked(self, event):
            global oval
            global player
            drawpad.move(player, 20, 0)
        #enemy number 1    
direction = 1
enemy1 = drawpad.create_rectangle(1,50,50,100, fill = "red")
def animate():
    global direction
    global enemy1
    x1, y1, x2, y2 = drawpad.coords(enemy1)
    if x2 > drawpad.winfo_width():
        direction = - 1
    elif x1 < 0: 
        direction = 1
    drawpad.move(enemy1,direction,0)
    drawpad.after(1,animate)

animate()
direction = 1
enemy2 = drawpad.create_rectangle(1,200,50,250, fill = "orange")
def animate1():
    global direction
    global enemy2
	#enemy number 2
       
    x1, y1, x2, y2 = drawpad.coords(enemy2)
    if x2 > drawpad.winfo_width():
        direction = - 1
    if x1 > drawpad.winfo_height(): 
        direction = 1
    drawpad.move(enemy2,direction,0)
    drawpad.after(20,animate1)
direction = 1   
animate1()
enemy3 = drawpad.create_rectangle(1,350,50,400, fill = "yellow")
def animate2():
    global direction
    global enemy3
	# enemy number 3
    
    x1, y1, x2, y2 = drawpad.coords(enemy3)
    if x2 > drawpad.winfo_width():
        direction = - 1
    if x1 > drawpad.winfo_height(): 
        direction = 1
    drawpad.move(enemy3,direction,0)
    drawpad.after(30,animate2)
    	
animate2()

app = MyApp(root)
root.mainloop()