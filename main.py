from tkinter import*
from tkinter.messagebox import askquestion
import makedtabase
# window
window = Tk()
db = makedtabase.database('D:/python project/database/newdatabase.db')
window.title('first project')
window.geometry('600x300')
window.resizable(0,0)
# function


def selecteditem(event):
    global select
    index = listbox_.curselection()
    select = listbox_.get(index)
    clear()
    Entry_name.insert(END,select[1])
    Entry_lastname.insert(END,select[2])
    Entry_city.insert(END,select[3])
    Entry_tell.insert(END,select[4])

    
def deleteitem():
    db.remove(select[0])
    clear()
    show_item()



def show_item():
    listbox_.delete(0,END)
    records = db.fetch()
    for i in records:
        listbox_.insert(END,i)



def add_to_listbox():
    db.insert(Entry_name.get() , Entry_lastname.get() , Entry_city.get() , Entry_tell.get() )
    listbox_.insert(END,(Entry_name.get() , Entry_lastname.get() , Entry_city.get() , Entry_tell.get()))
    clear()
    show_item()


def clear():
    Entry_name.delete(0,END)
    Entry_lastname.delete(0,END)
    Entry_city.delete(0,END)
    Entry_tell.delete(0,END)
    Entry_name.focus_set()
    


 


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
buttton_insert = Button(window,text='insert',width=10,command=add_to_listbox)
buttton_insert.place(x=500 , y= 120)

buttton_show = Button(window,text='show item',width=10,command=show_item)
buttton_show.place(x=500 , y= 160)

buttton_delete = Button(window,text='delete',width=10,command=deleteitem)
buttton_delete.place(x=400 , y= 160)

buttton_clear = Button(window,text='clear',width=10,command=clear)
buttton_clear.place(x=400 , y= 120)
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

listbox_.bind('<<ListboxSelect>>',selecteditem)

# mainloop
window.mainloop()
