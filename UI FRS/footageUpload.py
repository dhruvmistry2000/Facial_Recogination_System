from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.configure(background="white")
root.geometry("2000x1070")

root.title("Facial Recognition - Footage Upload")

Label(root,text="Footage Upload", font=("Roboto 24 bold underline"),pady=37, bg="white").grid(row=1,column=5,padx=100)

cameraId = Label(root, text="Camera Id :", font=("Roboto 17"), bg="white")
area = Label(root, text="Area :", font=("Roboto 17"), bg="white")
footage = Label(root, text="Footage Upload :", font=("Roboto 17"), bg="white")

cameraId.grid(row=3,column=4,pady=13,padx=(450,0), sticky=W)
area.grid(row=4,column=4,pady=13,padx=(450,0),sticky=W)
footage.grid(row=5,column=4,pady=13,padx=(450,0),sticky=W)

cameraValue = IntVar()
footageValue = IntVar()
areaValue = StringVar()

cameraIdEntry = Entry(root,width=40,borderwidth=5,relief=RIDGE,font=("Roboto 17"), textvariable=cameraValue)
areaEntry = Entry(root,width=40,borderwidth=5,relief=RIDGE,font=("Roboto 17"), textvariable=areaValue)

cameraIdEntry.grid(row=3, column=5,pady=13, sticky=W)
areaEntry.grid(row=4, column=5,pady=13, sticky=W)

footage = Checkbutton(text="Upload Here", variable=footageValue,font=("Roboto 17") , bg="white")
footage.grid(row=5, column=5,pady=13, sticky=W)

def getvals():
    print("Form submitted")
    with open("footageRecords.txt", "a") as f:
        f.write(f"{cameraValue.get(),footageValue.get(),areaValue.get()}\n")

Button(text="Footage Upload",bg="white",borderwidth=5,relief=RIDGE,font=("Roboto 17"), command=getvals).grid(row=7,column=5,pady=37)

root.mainloop()