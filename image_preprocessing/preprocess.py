import os
from PIL import Image
from config import config

img_files = []
for address, dirs, files in os.walk(config.root_directory):
    for name in files:
        file_name = f"./{address}/{name}"
        img_files.append(file_name)
