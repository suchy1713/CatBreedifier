import os
import glob
from PIL import Image
import numpy as np
import pandas as pd
import sys
import csv

directory = os.fsencode('images/cats')

X = []
y = []

for file in glob.iglob('images/cats/*'):
    print(file)
    image = Image.open(file).convert('RGB')
    X.append(np.asarray(image).tolist())
    filename = file.split('/')[2].split('_')

    if len(filename) == 2:
        y.append(filename[0])
    else:
        y.append(filename[0] + ' ' + filename[1])

df = pd.DataFrame(data={'X': X, 'y': y})

np.set_printoptions(threshold=sys.maxsize)
df.to_csv('data/cats.csv', index=False, quotechar='"', encoding='ascii')