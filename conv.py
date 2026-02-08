from tkinter import *
import convertFuncs as conv

def convert(x):
    label2.config(text="Binary: "+conv.convert_binary(x))
    label3.config(text="Octal: "+conv.convert_octal(x))
    label4.config(text="Hexadecimal: "+conv.convert_hexadecimal(x))
    
def init():
    global label2,label3,label4
    root=Tk()
    root.geometry("200x200")
    label1=Label(root,text="Enter: ")
    label1.pack()
    entry1=Entry(root)
    entry1.pack(padx=20,pady=20)
    button=Button(root,text="Convert",command=lambda:convert(int(entry1.get())))
    button.pack()
    label2=Label(root,text="Binary: ")
    label2.pack(padx=10,pady=2,anchor="w")
    label3=Label(root,text="Octal: ")
    label3.pack(padx=10,pady=2,anchor="w")
    label4=Label(root,text="Hexadecimal: ")
    label4.pack(padx=10,pady=2,anchor="w")
    root.mainloop()

if __name__ == "__main__":
    init()