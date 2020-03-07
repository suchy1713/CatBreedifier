import os
import glob
from PIL import Image
import numpy as np
import cv2

directory = 'images/cats_flickr'

#get all folder names
_, folder_names, _ = next(os.walk(directory))

#find an average size
#widths = []
#heights = []

#for folder in folder_names:
#    for file in glob.iglob(os.fsencode('images/cats_v2/'+folder+'/*')):
#        print(file)
#        image = Image.open(file)
#        widths.append(image.size[0])
#        heights.append(image.size[1])

#print(np.mean(widths)) #295
#print(np.mean(heights)) #305

#resize every picture to the average size
for folder in folder_names:
    for file in glob.iglob(os.fsencode('images/cats_flickr/'+folder+'/*')):
        file = file.decode("utf-8") 
        print(file)
        image = Image.open(file).convert('RGB')
        image = image.resize((300, 300))
        image.save(file)
