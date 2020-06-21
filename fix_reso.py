import os

file_names = os.listdir(r'/home/aadarsha/Documents/Python Tutorial')

for file_name in file_names:
	command = "ffmpeg -i '"+file_name+"' -vf scale=1920:1080 fixed/'"+file_name[:-4]+".mp4'"
	os.system(command)
	
