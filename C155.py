from tkinter import *
root=Tk()
root.title("Dictionary")
root.geometry("600x400")
label_1=Label(root)
label_2=Label(root)
label_3=Label(root)
label_1.place(relx=0.5,rely=0.4,anchor=CENTER)
label_2.place(relx=0.5,rely=0.6,anchor=CENTER)
label_3.place(relx=0.5,rely=0.8,anchor=CENTER)
dictionary={"Mutable":"Values can be changed just like a list","Immutable":"Values cannot be changed just like a Tuple","Tkinter":"It Is The GUI Library Of Python"}
def mut():
    label_1["text"]=dictionary["Mutable"]
def immut():
    label_2["text"]=dictionary["Immutable"]
def tkint():
    label_3["text"]=dictionary["Tkinter"]
button_1=Button(root,text="Meaning Of Mutable",command=mut)
button_2=Button(root,text="Meaning Of Immutable",command=immut)
button_3=Button(root,text="Meaning Of Tkinter",command=tkint)

button_1.place(relx=0.5,rely=0.3,anchor=CENTER)
button_2.place(relx=0.5,rely=0.5,anchor=CENTER)
button_3.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()