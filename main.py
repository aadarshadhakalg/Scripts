from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import shutil

class studymandu:

    def __init__(self, videos_folder,font_path,font_size,image_path):
        self.videos_folder = videos_folder
        self.font_path = font_path
        self.font_size = font_size
        self.image_path = image_path


    def title_in_image(self):

        file_names = os.listdir(r''+self.videos_folder)
        W, H = (1920, 1080)
        fnt = ImageFont.truetype(self.font_path, self.font_size)
        os.mkdir("temp")
        os.mkdir("temp/Images")

        for title in file_names:
            img = Image.open(self.image_path)
            d = ImageDraw.Draw(img)
            w, h = d.textsize(title, font=fnt)
            d.text(((W - w) / 2, (H - h) / 1.8), title[:-4], font=fnt, fill=(0, 0, 0))
            img.save('temp/Images/'+title[:-4] + '.png')

    def chapter_intros(self):
        file_names = os.listdir(r'temp/Images/')
        os.mkdir('temp/Chapter-Intros')


        for file_name in file_names:
            command = r"ffmpeg -loop 1 -i temp/Images/'"+file_name+"' -c:v libx264 -t 5 -pix_fmt yuv420p temp/out.mp4"
            os.system(command)
            clip1 = VideoFileClip("assets/intro.mp4")
            clip2 = VideoFileClip("temp/out.mp4")
            final_clip = concatenate_videoclips([clip1,clip2],method="chain")
            final_clip.write_videofile('temp/Chapter-Intros/'+file_name[:-4]+".mp4")
            os.remove("temp/out.mp4")

    def video_dimension_fixer(self):
        file_names = os.listdir(r''+self.videos_folder)
        os.mkdir("temp/Fixed")
        for file_name in file_names:
            command = "ffmpeg -i "+self.videos_folder+"'"+ file_name+"'" + " -vf scale=1920:1080 temp/Fixed/'" + file_name[:-4] + ".mp4'"
            os.system(command)

    def videoplusintroduction(self):
        file_names = os.listdir(r'temp/Fixed')
        intro_names = os.listdir(r'temp/Chapter-Intros')
        os.mkdir('Output')
        os.mkdir('Output/Final')

        for file_name in file_names:
            for intro_name in intro_names:
                if intro_name == file_name:
                    clip1 = VideoFileClip("temp/Chapter-Intros/"+intro_name)
                    clip2 = VideoFileClip("temp/Fixed/"+file_name)
                    final_clip = concatenate_videoclips([clip1,clip2])
                    final_clip.write_videofile("Output/Final/"+file_name)


    def clean(self):
        shutil.rmtree('temp')