from Tkinter import *
import Tkinter, tkFileDialog
import os, time
import shutil


def checkbuttonCallBack1():
	if cb_Var1 ==  1:
		formats.append('.jpeg')
	return

def checkbuttonCallBack2():
	if cb_Var1 == 1:
		formats.append('.mov')
		
	return



def askdirCallBack():
	e_var = tkFileDialog.askdirectory(initialdir = "/home")
	Entry_box.delete(0,END)
	Entry_box.insert(0, e_var)
	return

def organizeCallBack():
	# saving path of the current working directory in a variable
	cur_dir = Entry_box.get()
	print cur_dir
	# entering the files with .jpg and .mov extension in a list 'files'
	files = [f for f in os.listdir(cur_dir) if f.endswith('.jpg') or f.endswith('.mov')]
	

	# the following for loop access each file in the list one by one and move them in appropriate folders
	for file in files:
		cd = time.strftime("%Y%m%d", time.localtime(os.path.getmtime(os.path.join(cur_dir,file)))) # fetches the date of creation of file 
																			 					   # and convert the fetched date info
																			 					   # in to 'YYYYMMDD' format string 
		
		# the following if/elif checks if the file extension is .jpg or .mov and move the file in appropriate folders
		if file.endswith(".jpg"):
			pic_dir = os.path.join(cur_dir, os.path.join('jpg', cd)) # path to which the jpg files are copied
																	 # eg: 'jpg/20140628' in the current directory
			
			src_dir = os.path.join(cur_dir, file) 					 # source directory/file
			if not os.path.exists(pic_dir):							 # checks if directory exist and - 
				os.makedirs(pic_dir)								 # create directory if it does not exist and -
				shutil.move(src_dir, pic_dir)	 					 # move the file to newly created folder
			else:
				shutil.move(src_dir, pic_dir)						 # if folder already exist move the file to -
																	 # that folder directly
			
		# this 'elif' do the same process as above mentioned 'if' block, but for .mov files
		elif file.endswith(".mov"):									 
			mov_dir = os.path.join(cur_dir, os.path.join('mov', cd))
			src_dir = os.path.join(cur_dir, file)
			if not os.path.exists(mov_dir):
				os.makedirs(mov_dir)
				shutil.move(src_dir, mov_dir)
			else:
				shutil.move(src_dir, mov_dir)


formats = []
root = Tkinter.Tk()
root.title("File Organizer")
root.geometry("350x150")
cb_Var1 = BooleanVar()
cb_Var2 = BooleanVar() 
e_var = StringVar()
jpeg_cb = Checkbutton(root, text = ".jpeg", variable = cb_Var1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 5, command = checkbuttonCallBack1)
mov_cb = Checkbutton(root, text = ".mov", variable = cb_Var2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 5, command = checkbuttonCallBack2)
jpeg_cb.grid(row = 0, column = 0)
mov_cb.grid(row = 0, column = 1)
Entry_box = Entry(root, bd =3, textvariable = e_var)
Entry_box.grid(row = 1, columnspan = 2)
Browse_button = Tkinter.Button(root, text ="Browse Folder", command = askdirCallBack)
Browse_button.grid(row = 1, column = 3)
Organize_button = Tkinter.Button(root, text ="Organize", command = organizeCallBack)
Organize_button.grid(row = 2, column = 0, columnspan = 3)




root.mainloop()
