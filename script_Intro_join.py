from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


file_names = os.listdir(r'/home/aadarsha/Documents/Python Tutorial/fixed')
intro_names = os.listdir(r'/home/aadarsha/Documents/Python Tutorial/intros')

for file_name in file_names:
	for intro_name in intro_names:
		if intro_name == file_name:
			clip1 = VideoFileClip("intros/"+intro_name)
			clip2 = VideoFileClip("fixed/"+file_name)
			final_clip = concatenate_videoclips([clip1,clip2])
			final_clip.write_videofile("final/"+file_name)
