import os 
import imageio


file_list = sorted(os.listdir("tamrin8/images"))

image = []
for file_name in file_list:
    file_path = "tamrin8/images/" + file_name
    gif = imageio.v2.imread(file_path)
    image.append(gif)

imageio.mimsave("output.gif", image)