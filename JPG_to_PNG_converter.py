import os
from PIL import Image

# Point to folder with JPG images
jpg_folder = input('Copy and paste absolute path to the folder with JPG images: ')
jpg_folder = jpg_folder.replace('\\', '\\\\')


# Point to folder where converted images will be saved
png_folder = input('Copy and paste absolute path to the folder where PNG images will be stored: ')
png_folder = png_folder.replace('\\', '\\\\')


# Check if both folders exist
if not os.path.exists(jpg_folder):
    jpg_folder = input("The path to the JPG folder does not exist. Enter correct path: ")
    jpg_folder = jpg_folder.replace('\\', '\\\\')

if not os.path.exists(png_folder):
    os.mkdir(png_folder)
    print(f"Created the folder {png_folder}")

# Loop through JPG images
for img in os.listdir(jpg_folder):
    img_path = f'{jpg_folder}\\{img}'
    image = Image.open(img_path)
    name = os.path.splitext(img)[0]
    # Convert to PNG and save converted images
    image.save(f'{png_folder}\\{name}.png', 'png') 

print('All images are converted!')
