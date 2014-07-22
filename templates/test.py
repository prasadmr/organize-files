
	cur_dir = Entry_box.get()
	print cur_dir
	
	files = [f for f in os.listdir(cur_dir) if f.endswith('.jpg') or f.endswith('.mov')]
	

	
	for file in files:
		cd = time.strftime("%Y%m%d", time.localtime(os.path.getmtime(os.path.join(cur_dir,file)))) 
		if file.endswith(".jpg"):
			pic_dir = os.path.join(cur_dir, os.path.join('jpg', cd)) 
			
			src_dir = os.path.join(cur_dir, file) 					 
			if not os.path.exists(pic_dir):							 
				os.makedirs(pic_dir)								 
				shutil.move(src_dir, pic_dir)	 					 
			else:
				shutil.move(src_dir, pic_dir)						 
																	 
			