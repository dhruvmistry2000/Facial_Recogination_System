from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile 
from tkinter.filedialog import asksaveasfile 
import time
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import numpy as np
import os
import PIL  

root = Tk()
root.configure(background="white")
root.geometry("2000x1070")

root.title("Facial Recognition - Data Upload")

Label(root,text="Details About Criminal", font=("Roboto 24 bold underline"),pady=27, bg="white").grid(row=1,column=5,padx=100)
Label(root,text="Crime Information", font=("Roboto 24 underline"),pady=70, bg="white").grid(row=6,column=5)

name = Label(root, text="Name :", font=("Roboto 17"), bg="white")
gender = Label(root, text="Gender :", font=("Roboto 17"), bg="white")
photo = Label(root, text="Photo :", font=("Roboto 17"), bg="white")
crime = Label(root, text="Crime :", font=("Roboto 17"), bg="white")
city = Label(root, text="City :", font=("Roboto 17"), bg="white")
regname = Label(root, text="Registered station name :", font=("Roboto 17"), bg="white")
doc = Label(root, text="Date Of Crime :", font=("Roboto 17"), bg="white")

name.grid(row=2,column=4,pady=13,padx=(450,0), sticky=W)
gender.grid(row=3,column=4,pady=13,padx=(450,0),sticky=W)
photo.grid(row=4,column=4,pady=13,padx=(450,0),sticky=W)
crime.grid(row=7,column=4,pady=13,padx=(450,0),sticky=W)
city.grid(row=8,column=4,pady=13,padx=(450,0),sticky=W)
regname.grid(row=9,column=4,pady=13,padx=(450,0),sticky=W)
doc.grid(row=10,column=4,pady=13,padx=(450,0),sticky=W)

nameValue = StringVar()
photoValue = IntVar()
crimeValue = StringVar()
cityValue = StringVar()
regnameValue = StringVar()
docValue = StringVar()

nameEntry = Entry(root,width=40,borderwidth=5,relief=RIDGE,font=("Roboto 17"), textvariable=nameValue)
crimeEntry = Entry(root, width=40,borderwidth=5,relief=RIDGE,font=("Roboto 17"),textvariable=crimeValue)
# cityEntry = Entry(root,width=40,borderwidth=5,relief=RIDGE,font=("Roboto 17"), textvariable=cityValue)
regnameEntry = Entry(root,width=40,borderwidth=5,relief=RIDGE,font=("Roboto 17"), textvariable=regnameValue)
docEntry = Entry(root,width=40,borderwidth=5,relief=RIDGE,font=("Roboto 17"), textvariable=docValue)

nameEntry.grid(row=2, column=5,pady=13, sticky=W)
crimeEntry.grid(row=7, column=5,pady=13, sticky=W)
# cityEntry.grid(row=8, column=5,pady=13, sticky=W)
regnameEntry.grid(row=9, column=5,pady=13, sticky=W)
docEntry.grid(row=10, column=5,pady=13, sticky=W)

#Checkbox and packing it
# photo = Checkbutton(text="Upload Here", variable=photoValue,font=("Roboto 17") , bg="white")
# photo.grid(row=4, column=5,pady=13, sticky=W)

# list=['Male','Female','Other']
#  genderlist = OptionMenu(root,genderValue, *list)
# genderlist.config(width=50,font=("Roboto 17"), bg="white")
# genderValue.set("--Select--")

# Adding combobox drop down list for gender selection
genderValue = StringVar()
genderlist = ttk.Combobox(root, width = 39,font=("Roboto 17"), textvariable = genderValue)
genderlist['values'] = ('Female','Male','Other')
genderlist.grid(row=3, column=5, sticky=W)
genderlist.current()

# Adding combobox drop down list for city 
citylist = ttk.Combobox(root, width = 39,font=("Roboto 17"), textvariable = cityValue)
citylist['values'] = ('Ahmedabad','Vadodara','Anand','Chhota Udaipur','Dahod','Dahod','Kheda','Mahisagar','Panchmahal','Gandhinagar','Aravalli','Banaskantha','Mehsana','Patan','Sabarkantha','Saurashtra - Kutch','Rajkot','Amreli','Bhavnagar','Botad','Devbhoomi Dwarka','Gir Somnath','Jamnagar','Junagadh','Morbi','Porbandar','Surendranagar','Kachchh','Surat','Bharuch','Dang','Narmada',
'Navsari','Tapi','Valsad')
citylist.grid(row=8, column=5, sticky=W)
citylist.current()


#To get the values when user click on upload and store it in file records.txt 
def getvals():
    print("Form submitted")
    # print(f"{nameValue.get(),genderValue.get(),crimeValue.get(),cityValue.get(),regnameValue.get(),docValue.get()}")
    with open("dataRecords.txt", "a") as f:
        f.write(f"{nameValue.get(),genderValue.get(),crimeValue.get(),cityValue.get(),regnameValue.get(),docValue.get()}\n")


Button(text="Data Upload",bg="white",borderwidth=5,relief=RIDGE,font=("Roboto 17"), command=getvals).grid(row=13,column=5,pady=37)


#For saving the uploaded image in a folder

def open_file():
    file_path = askopenfile(mode='w', filetypes=[('Image Files', '*png')])
    if file_path:
        filepath = os.path.abspath(file_path.name)
    #     print(filepath)
    # f = asksaveasfile(initialfile="E:\\tkinter\Tkinter" ,defaultextension=".png",filetypes=[("All Files","*.*"),("Text Documents","*.png")])
    picture = Image.open(r'file.png')  
    picture = picture.save(filepath)

def uploadFiles():
    pb1 = ttk.Progressbar(
        root, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        

dlbtn = Button(
    root, 
    text ='Choose File ', 
    command = lambda:open_file()
    ) 
dlbtn.grid(row=1, column=1)


upld = Button(
    root, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)



root.mainloop()