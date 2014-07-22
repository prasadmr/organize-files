from Tkinter import *
import Tkinter, tkFileDialog
import os, time
import shutil


def askdirCallBack():
	e_var = tkFileDialog.askdirectory(initialdir = "/home")
	Entry_box.delete(0,END)
	Entry_box.insert(0, e_var)
	return


def organizeCallBack():
	cur_dir = ''
	formats = []
	string1 = str(formats_ip.get(1.0, END))
	formats = string1.split(', ')
	formats[:] = [x.rstrip('\n') for x in formats]
	cur_dir = Entry_box.get()
	
	for i in formats:
		files = [f for f in os.listdir(cur_dir) if f.endswith(i)]
		for file in files:
			cd = time.strftime("%Y%m%d", time.localtime(os.path.getmtime(os.path.join(cur_dir,file)))) 
			directory = os.path.join(cur_dir, os.path.join(i, cd)) 
			
			src_dir = os.path.join(cur_dir, file) 					
			if not os.path.exists(directory):							 
				os.makedirs(directory)								 
				shutil.move(src_dir, directory)	 					 
			else:
				shutil.move(src_dir, directory)						 
			

root = Tkinter.Tk()
root.title("File Organizer")
root.geometry("350x200")
e_var = StringVar()
fip_var = StringVar()
Entry_box = Entry(root, bd =3, textvariable = e_var)
Entry_box.grid(row = 0, columnspan = 2)
Browse_button = Tkinter.Button(root, text ="Browse Folder", command = askdirCallBack)
Browse_button.grid(row = 0, column = 3)
formats_ip = Text(root, width = 20, height = 10)
formats_ip.grid(row = 1, columnspan = 2, rowspan = 5)
Organize_button = Tkinter.Button(root, text ="Organize", command = organizeCallBack)
Organize_button.grid(row = 1, column = 3)


root.mainloop()