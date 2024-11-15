from tkinter import *
from googletrans import Translator

def translate():
    message = text1.get('1.0', 'end-1c')
    trans = Translator()
    output = trans.translate(text=message,src='en',dest='th')
    text2.insert('end',output.text)
def clear():
    text1.delete(1.0,'end')
    text2.delete(1.0,'end')
    
root = Tk()
root.title("Sk4let Translate (EN_TH)")
root.geometry('530x300')
root.maxsize(530,300)
root.minsize(530,300)

#widget
label=Label(text="English - Thai",font=('Arial',25,'bold'))
label.place(x=150,y=20)
text1 = Text(root,width="30",height="10")
text1.place(x=10,y=70)
text2 = Text(root,width="30",height="10")
text2.place(x=260,y=70)
translateBtn = Button(root,text=("แปลภาษา"),command=translate)
translateBtn.place(x=180,y=250)
clearBtn = Button(root,text=("เคลียร์"),command=clear)
clearBtn.place(x=280,y=250)

root.mainloop()