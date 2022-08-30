from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def conversion(text='type', src='English', dest='Hindi'):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0, END)
    text_get = conversion(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, text_get)


root = Tk()
root.title("Translator")
root.geometry("400x600")
root.config(bg='green')

lab_txt = Label(root, text="Translator", font=("Time New Roman", 30), fg='blue')
lab_txt.place(x=100, y=50, height=50, width=200)

lab_txt.config(bg='pink')

lab_txt = Label(root, text="Source text", font=("Time New Roman", 15), fg="red")
lab_txt.place(x=100, y=115, height=20, width=200)
lab_txt.config(bg='yellow')

frame = Frame(root).pack(side=BOTTOM)

sor_txt = Text(frame, font=("Time New Roman", 20), wrap=WORD)
sor_txt.place(x=10, y=145, height=70, width=380)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10, y=215, height=30, width=120)
comb_sor.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=162, y=216, height=30, width=80)

comb_dest = comb_sor = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=270, y=215, height=30, width=120)
comb_dest.set("English")

lab_txt = Label(root, text="Destination text", font=("Time New Roman", 15), fg="red")
lab_txt.place(x=100, y=300, height=20, width=200)
lab_txt.config(bg='yellow')

dest_txt = Text(frame, font=("Time New Roman", 20), wrap=WORD)
dest_txt.place(x=10, y=330, height=70, width=380)

root.mainloop()
