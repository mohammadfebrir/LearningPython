import os

def rename_file():
	file_list=os.listdir(r"/home/visionet/Public/python/prank/prank/")
	save_path=os.getcwd();

	os.chdir(r"/home/visionet/Public/python/prank/prank/")
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(save_path)

rename_file()