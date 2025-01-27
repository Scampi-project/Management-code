# coding : utf-8
from tkinter import*
from datetime import*

"""
b=datetime.now()
print (type(b))
c=datetime.now()
b=(c-b).total_seconds()//300
print(b)
"""

def valider():
	global a
	a=entree.get()
	
a=5
fenetre=Tk()
focus= Label(fenetre, text="focus length in cm")
entree=Entry(fenetre,textvariable=StringVar,width=30)
focus.pack()
entree.pack()
bouton=Button(fenetre,text="valid",command=valider)
bouton.place(x=60,y=160)
print (a)
fenetre.mainloop()

