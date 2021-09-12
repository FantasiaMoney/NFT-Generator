from PIL import Image
from PIL import ImageOps
import random
import os
import csv

input_dir = r'C:\Users\PC\Desktop'
input_dogs_data = 'dogs-data.csv'
input_folder_dogs = 'dogs images'
input_folder_glass = 'glasses images'
output_dir = r'C:\Users\PC\Desktop'
output_folder = 'Combined Images'

in_csv = csv.reader(open(os.path.join(input_dir, input_dogs_data), 'r'))
in_rows = list(in_csv)
in_rows.pop(0)

#glass_resize_width = 30
#glass_resize_height = 15
#glass_width_index = 23
#glass_height_index = 25
#resize_width = 300
#resize_height = 500

if not os.path.exists(os.path.join(output_dir, output_folder)):
    os.mkdir(os.path.join(output_dir, output_folder))
else:
    pass
    
# function to stretch or condense image    
def resize(image, d, basewidth, baseheight):
    img = Image.open(os.path.join(output_dir, output_folder, "{}.png".format(str(d))))
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, hsize), Image.ANTIALIAS)
    img.save(os.path.join(output_dir, output_folder, "resized_{}.png".format(str(d))), 'PNG')
    
    
input_dogs = os.listdir(os.path.join(input_dir, input_folder_dogs))
input_glass = os.listdir(os.path.join(input_dir, input_folder_glass))


for d in range(0, len(input_dogs)):
    input_dog_folder = input_dogs[d].replace('.png', '')
    for r in range(0, len(in_rows)):
        if input_dog_folder==in_rows[r][0]:
            current_dog_row = in_rows[r]
        else:
            pass
    eye_position_width = int(float(current_dog_row[1]))
    eye_position_height = int(float(current_dog_row[2]))
    glass_size_width = int(float(current_dog_row[7]))
    glass_size_height = int(float(current_dog_row[8]))
    
    if not os.path.exists(os.path.join(output_dir, output_folder, input_dog_folder)):
        os.mkdir(os.path.join(output_dir, output_folder, input_dog_folder))
    else:
        pass
    dog_image = Image.open(os.path.join(input_dir, input_folder_dogs, input_dogs[d]))
    for g in range(0, len(input_glass)):
    
        glass_image = Image.open(os.path.join(input_dir, input_folder_glass, input_glass[g]))
        dog_image = dog_image.convert('RGBA')
        glass_image = glass_image.convert('RGBA')
        glass_image = glass_image.resize((glass_size_width, glass_size_height))
        

        # Transparency
        newImage = []
        for item in glass_image.getdata():
            if item[:3] == (255, 255, 255):
                newImage.append((255, 255, 255, 0))
            else:
                newImage.append(item)
        glass_image.putdata(newImage)
        dog_image.paste(glass_image, (eye_position_width,eye_position_height), glass_image)
        dog_image.save(os.path.join(output_dir, output_folder, input_dog_folder, "{}.png".format(str(g))),"PNG")
    #resized_dog_image = resize(dog_image, d, resize_width, resize_height)


