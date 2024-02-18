from tkinter import*
from tkinter.messagebox import askquestion
import makedtabase
# window
window = Tk()
db = makedtabase.database('D:/python project/database/contacts.db')
window.title('first project')
window.geometry('600x300')
window.resizable(0,0)
# function

def insert():
    inserttocontacts()
    gettell = int(Entry_tell.get())
    getcity = Entry_city.get()
    getlastname = Entry_lastname.get()
    getname = Entry_name.get()
    listbox_.insert(END,f'{getname},{getlastname},{getcity},{gettell}')
    clear()
    


def clear():
    Entry_name.delete(0,END)
    Entry_lastname.delete(0,END)
    Entry_city.delete(0,END)
    Entry_tell.delete(0,END)
    Entry_name.focus_set()
    
def inserttocontacts():
    db.insertcontact( Entry_name.get() , Entry_lastname.get() , Entry_tell.get() , Entry_city.get() )
     
   
def delete():
    res = askquestion('delete','are you sure?!!')
    if res == True:
        listbox_.delete(listbox_.curselection())
    clear()


def fetch():
    clear()
    item = listbox_.get(listbox_.curselection()).split(',')
    Entry_name.insert(0,item[0])
    Entry_lastname.insert(0,item[1])
    Entry_city.insert(0,item[2])
    Entry_tell.insert(0,item[3])
    
    
    
    


# labels and buttons
label_name = Label(window,text= 'name:')
label_name.place(x= 20 , y= 10)

label_lastname = Label(window,text= 'lastname:')
label_lastname.place(x= 300 , y= 10)

label_city = Label(window,text= 'city:')
label_city.place(x= 20 , y= 70)

label_tell = Label(window,text= 'tell:')
label_tell.place(x= 300 , y= 70)

# buttoms
buttton_insert = Button(window,text='insert',width=10,command=insert)
buttton_insert.place(x=500 , y= 120)

buttton_fetch = Button(window,text='fetch',width=10,command=fetch)
buttton_fetch.place(x=500 , y= 160)

buttton_delete = Button(window,text='delete',width=10,command=delete)
buttton_delete.place(x=500 , y= 200)

buttton_clear = Button(window,text='clear',width=10,command=clear)
buttton_clear.place(x=500 , y= 240)
# entrys
Entry_name = Entry(window)
Entry_name.place(x=70,y=10)


Entry_lastname = Entry(window)
Entry_lastname.place(x=370,y=10)


Entry_city = Entry(window)
Entry_city.place(x=70,y=70)


Entry_tell = Entry(window)
Entry_tell.place(x=350,y=70)


# listbox
listbox_ = Listbox(window,width=40,height=9,font='arial 11')
listbox_.place(x=80,y=100)


# mainloop
window.mainloop()
