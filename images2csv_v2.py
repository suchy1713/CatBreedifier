import os
import glob
from PIL import Image
import numpy as np
import pandas as pd
import sys
import csv

directory = 'images/cats_v2'
_, folder_names, _ = next(os.walk(directory))
directory = os.fsencode('images/cats_v2')

np.set_printoptions(threshold=sys.maxsize)

i = 0
j = 0
for folder in folder_names:
        X = []
        y = []
        for file in glob.iglob('images/cats_v2/'+folder+'/*'):
                print(i, ': ', file)
                i += 1
        
                image = Image.open(file).convert('RGB')
                X.append(np.asarray(image))
                y.append(folder)

        if j == 0:
                df = pd.DataFrame(data={'X': X, 'y': y})
        else:
                df = pd.concat([pd.read_csv('data/cats_v2.csv'), pd.DataFrame(data={'X': X, 'y': y})])
        df.to_csv('data/cats_v2.csv', index=False, quotechar='"', encoding='ascii')
        j += 1