import tkinter
import tkinter.messagebox
import pickle


window=tkinter.Tk()
window.title("To-Do List")
window.config(bg='pink')
frame=tkinter.Frame(window)
frame.pack(pady=10)



def task_adding():
    todo=task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention !!",message="please enter some task")


def task_removing():
    try:
        todo_box.delete(tkinter.ANCHOR)
    except:
        tkinter.messagebox.showwarning(title="Attention !!",message="select a task to delete")


def task_load():
    try:
            
        with open("tasks.dat","rb") as file:
         todo_list=pickle.load(FileExistsError)
        todo_box.delete(0,tkinter.END)
        for todo in todo_list:
            todo_box.insert(tkinter.END,todo)
    except:
         tkinter.messagebox.showwarning(title="Attention !!",message="can't select a task")




todo_box=tkinter.Listbox(frame,height=8,width=25,font='Times',selectbackground='black')
todo_box.pack(side=tkinter.LEFT,fill=tkinter.BOTH) 

scroller=tkinter.Scrollbar(frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)


todo_box.config(yscrollcommand=scroller.set)


task_list=["Wake up"," Gym"," Yoga",]
for item in task_list:
   todo_box.insert( tkinter.END, item)


task_add=tkinter.Entry(window,width=70)
task_add.pack()

add_button=tkinter.Button(window,text="Add   Task ",
    font=('times 14'),
    bg='paleturquoise',
    padx=20,
    pady=10,command=task_adding)
add_button.pack()

remove_button=tkinter.Button(window,text='Delete Task',
    font=('times 14'),
    bg='yellow',
    padx=20,
    pady=10,command=task_removing)
remove_button.pack()






window.mainloop()