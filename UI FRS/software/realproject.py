#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
# from matplotlib import image

root = Tk()
root.geometry("2000x1070")

f1=Frame(root,bg="black",borderwidth=4,relief=SUNKEN)
f1.pack(side=TOP,fill="x")

def hello():
    print("b1 click")

b1=Button(f1,fg="red",text="Buttton 1",command=hello)
b1.pack(side=LEFT)
b1.grid(padx=(500,0),pady=(0,0))



canvas= Canvas(root, width= 1400, height= 720)
canvas.pack()

img= (Image.open("photo1.png"))
resized_image= img.resize((800,720), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
bg=canvas.create_image(300,10, anchor=NW, image=new_image)

img1=ImageTk.PhotoImage(Image.open("learnmore.png"))

def cmd(event):
    print("run1 correctly")
img1=(Image.open("photo2.png"))  

resized_image1= img1.resize((100,30), Image.ANTIALIAS)
new_image1= ImageTk.PhotoImage(resized_image1)
bg1=canvas.create_image(370,420, anchor=NW, image=new_image1)

# Button=canvas.create_image(370,450,image=img1)
canvas.tag_bind(bg1,"<Button-1>",cmd) 

def cmd(event):
    print("run2 correctly")
img1=(Image.open("photo2.png"))  

resized_image2= img1.resize((100,30), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)
bg2=canvas.create_image(710,610, anchor=NW, image=new_image2)

# Button=canvas.create_image(370,450,image=img1)
canvas.tag_bind(bg2,"<Button-1>",cmd) 



root.mainloop()