import os
import glob
from PIL import Image
import numpy as np

directory = os.fsencode('images')

#separate cats from dogs
for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename[0].isupper():
        os.rename('images/'+filename, 'images/cats/'+filename)
        print(filename)

#find the smallest size
directory = os.fsencode('images/cats')

min_width = np.inf
min_height = np.inf

for file in glob.iglob('images/cats/*'):
    image = Image.open(file)

    if image.size[0] < min_width: min_width = image.size[0] 
    if image.size[1] < min_height: min_height = image.size[1] 


#resize every picture to the smallest size
for file in glob.iglob('images/cats/*'):
    print(file)
    image = Image.open(file).convert('RGB')
    
    image = image.resize((100, 100))
    image.save(file)