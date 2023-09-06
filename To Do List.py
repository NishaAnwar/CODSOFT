
from tkinter import *


root = Tk()
root.title("To-Do-List-App")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_List = []
                             ########################Functionalities#############################
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_List.append(task)
        list_box.insert(END, task)

def delete_task():
    global task_List
    task = str(list_box.get(ANCHOR))
    if task in task_List:
        task_List.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_List:
                taskfile.write(task + "\n")
        list_box.delete(ANCHOR)

def openTaskfile():
    try:
        global task_List
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != "\n":
                task_List.append(task)
                list_box.insert(END, task)
    except:
        file = open("tasklist.txt", "w")
        file.close()






def edit_task():
    selected_index = list_box.curselection()
    if selected_index:
        selected_index = selected_index[0]
        selected_task = task_List[selected_index]
        task_entry.delete(0, END)
        task_entry.insert(0, selected_task)

def update_task():
    selected_index = list_box.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_task = task_entry.get()
        if new_task:
            list_box.delete(selected_index)
            list_box.insert(selected_index, new_task)
            task_List[selected_index] = new_task
            task_entry.delete(0, END)
            with open("tasklist.txt", "w") as taskfile:
                for task in task_List:
                    taskfile.write(task + "\n")

                      ##############################Frames#########################
frame=Frame(root,width=500,height=150,bg="#FF8552")
frame.place(x=0,y=0)
label=Label(root,text="To Do List",font="Stylus 40 bold  ",bg="#FF8552",fg="white")
label.place(x=75,y=55)

frame1 = Frame(root, width=400, height=50, bg="grey")
frame1.place(x=0, y=150)




frame2 = Frame(root, bd=3, width=700, height=400, bg="#FF8552")
frame2.place(x=0,y=210)

# Entry
task=StringVar()
task_entry=Entry(frame1,width=18,font="arial 20 ",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
# Button
button = Button(frame1, text="ADD", font="arial 20 bold", width=6, bg="teal", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=5)

# List box
list_box = Listbox(frame2, font=("arial", 12), width=40, height=18, bg="grey", fg="white", cursor="hand2", selectbackground="#5a95ff")
list_box.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=BOTH)
list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

openTaskfile()

# Delete Button
delete_button=Button(root, text="DELETE", font="arial 18 bold", bg="teal", fg="white", bd=0, command=delete_task)
delete_button.pack(side=BOTTOM, pady=10)
delete_button.place(x=270,y=575)
#Edit Button
edit_button=Button(root, text=" EDIT ", font="arial 18 bold", bg="teal", fg="white", bd=0, command=edit_task)
edit_button.pack(side=BOTTOM, pady=10)
edit_button.place(x=160,y=575)

# Update Button
update_button=Button(root, text="UPDATE", font="arial 18 bold", bg="teal", fg="white", bd=0, command=update_task)
update_button.pack(side=BOTTOM, pady=10)
update_button.place(x=20,y=575)

root.mainloop()


