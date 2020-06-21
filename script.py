from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

#file_names = os.listdir(r'/home/aadarsha/Desktop/Images')

#print(file_names)

#for file_name in file_names:
command = "ffmpeg -loop 1 -i Attributes.png -c:v libx264 -t 5 -pix_fmt yuv420p out.mkv"
os.system(command)
clip1 = VideoFileClip("/home/aadarsha/Desktop/intro.mp4")
clip2 = VideoFileClip("out.mkv")
final_clip = concatenate_videoclips([clip1,clip2],method="chain")
final_clip.write_videofile("Attributes.mp4")
