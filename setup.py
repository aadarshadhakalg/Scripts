from main import studymandu

print(r"########### Welcome to Studymandu Uploaders Script #############")

print("RULES:\n")
print("\n1. Should not be the same path where script is running.")
print("2. Should not contain any other items except course videos.")
print("3. Video should have proper naming \n")
print("4. Directory path should end with backward slash \n")

videos_folder = input("Enter path of directory containing the video files (1920 x 1080) : ")
font_path = input("Enter path of of the font file: ")
font_size = int(input("Enter size of of the font: "))
image_path = input("Enter path of of the image file (1920 x 1080) : ")


run = studymandu(videos_folder,font_path,font_size,image_path)

run.title_in_image()
run.chapter_intros()
run.video_dimension_fixer()
run.videoplusintroduction()
run.clean()


