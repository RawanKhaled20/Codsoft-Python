"""/** author: Rawan Khaled  https://github.com/RawanKhaled20/Codsoft-Python.git"""

import tkinter as tk

# Create the GUI for the user
root = tk.Tk()
root.title("Prepare Your To-Do List")
root.geometry("500x700")
root.resizable(False, False)

task_list = []

#Add task function
def addTask():
    task=task_entry.get()
    task_entry.delete(0,"end")

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert("end", task)

# Delete task function
def deleteTask():
    global task_list
    task=str(listbox.get("anchor"))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete("anchor")

# Add icon to the prepare to-do list
image_icon = tk.PhotoImage(file="task.png")
root.iconphoto(False, image_icon)

# Set the background color for the main window
root.configure(bg="#CFC3C8")  # Use your desired background color

# Add top bar for a more classy look
top_image = tk.PhotoImage(file="topbar.png")
top_label = tk.Label(root, image=top_image, bg="#CFC3C8" )
top_label.place(relx=0.5, rely=0, anchor=tk.N)  # Place the top bar at the top and center

#Add Dock
Dock_Image=tk.PhotoImage(file="dock.png")
Dock_Label=tk.Label(root, image=Dock_Image, bg="#32405b")
Dock_Label.place(x=60, y=25)

#Add the Note image at the other side of the dock
Note_Image=tk.PhotoImage(file="task.png")
Note_Label=tk.Label(root, image=Note_Image, bg="#32405b")
Note_Label.place(x=400, y=25)

# Add a title heading
heading=tk.Label(root, text="All Task", font="Arial 20 bold ", fg="white", bg="#32405b")
heading.place(x=190, y=20)

#Main Entry frame
frame=tk.Frame(root, width=500, height=50, bg="white")
frame.place(x=0, y=180)

#Insert string
task= tk.StringVar()
task_entry=tk.Entry(frame, width=18, font="Arial 20 bold", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# The add button to add your tasks for the list
button=tk.Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#32405b", fg="#fff", bd=0, command=addTask)
button.place(x=400,y=0)

# Create the listbox
frame1= tk.Frame(root,bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(270,0), fill="both", expand=True)

listbox= tk.Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack( side="left", fill="both", padx=2, expand=True)

#Scroll bar for al big list in vertical
scroll_bar=tk.Scrollbar(frame1, orient="vertical")
scroll_bar.pack(side="right", fill="y", expand=False)
listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)

#Scroll bar for al big list in horizontal
scroll_bar2=tk.Scrollbar(listbox, orient="horizontal")
scroll_bar2.pack(side="bottom", fill="x", expand=False)
listbox.config(xscrollcommand=scroll_bar2.set)
scroll_bar2.config(command=listbox.xview)

#To delete an added task
Delete_Iamge=tk.PhotoImage(file="delete.png")
Delete_Label=tk.Button(root,image=Delete_Iamge, bd=0, bg="#CFC3C8", command=deleteTask)
Delete_Label.pack(side="bottom", pady=13)

root.mainloop()


"""
Extra details 
# Add background image
back_image = tk.PhotoImage(file="hard-chrome.png")
background_label = tk.Label(root, image=back_image)
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the background image at the center
background_label.place(relwidth=1, relheight=1)  # Stretch the background to fill the entire window
"""







