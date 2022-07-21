from tkinter import* 
from PIL import ImageTk, Image
import os
from tkinter import filedialog
import webbrowser

root = Tk()
root.minsize(900,900)
root.title("NOTEPAD")
root.configure(bg = "gray87")

open_img = ImageTk.PhotoImage(Image.open ('open.png'))
run_img = ImageTk.PhotoImage(Image.open ('run.png'))
save_img = ImageTk.PhotoImage(Image.open ('save.png'))

name = ""
def open_file():
    global name
    area.delete(1.0,END)
    entry.delete(0,END)
    text_file = filedialog.askopenfilename(title = "Open Text File", filetypes = (("Text Files","*.html"),))
    
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    entry.insert(END, formated_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    area.insert(END,paragraph)
    text_file.close()
    
    
def save():
    input_name = entry.get()
    file = open(input_name+".html","w")
    data = area.get(1.0, END)
    print(data)
    file.write(data)
    entry.delete(0,END)
    area.delete(1.0, END)
    messagebox.showinfo("Update","Success")
    
def run_file():
    global name
    webbrowser.open(name)
    
    

Open = Button(root, command=open_file)
Open.place(relx = 0.075, rely = 0.075, anchor = CENTER)

Save = Button(root, command=save)
Save.place(relx = 0.15, rely = 0.075, anchor = CENTER)

Run = Button(root, command=run_file)
Run.place(relx = 0.22, rely = 0.075, anchor = CENTER)

Open['image'] = open_img
Save['image'] = save_img
Run['image'] = run_img




Label1 = Label(root, text = "FILE NAME")
Label1.place(relx = 0.4, rely = 0.075, anchor = CENTER)

entry = Entry(root)
entry.place(relx = 0.6, rely = 0.075, anchor = CENTER)

area = Text(root)
area.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()