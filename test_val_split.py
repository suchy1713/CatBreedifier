import os
import glob
from PIL import Image
import numpy as np
from shutil import copyfile

directory = 'images/cats_v2'
_, folder_names, _ = next(os.walk(directory))

#separate cats from dogs
for folder in folder_names:
    for file in glob.iglob(os.fsencode('images/cats_v2/'+folder+'/*')):
        filename = os.fsdecode(file).split('/')[-1]
        if np.random.rand() <= 0.25:
            if not os.path.exists('images/cats_splitted/validation/'+folder+'/'):
                os.makedirs('images/cats_splitted/validation/'+folder+'/')
            copyfile('images/cats_v2/'+folder+'/'+filename, 'images/cats_splitted/validation/'+folder+'/'+filename)
        else:
            if not os.path.exists('images/cats_splitted/train/'+folder+'/'):
                os.makedirs('images/cats_splitted/train/'+folder+'/')
            copyfile('images/cats_v2/'+folder+'/'+filename, 'images/cats_splitted/train/'+folder+'/'+filename)

    #if filename[0].isupper():
     #   os.rename('images/'+filename, 'images/cats/'+filename)
      #  print(filename)