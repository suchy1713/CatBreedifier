import os
import glob
from PIL import Image
import numpy as np
import pandas as pd
import sys

directory = os.fsencode('images/cats')

X = []
y = []

for file in glob.iglob('images/cats/*'):
    print(file)
    image = Image.open(file).convert('RGB')
    X.append(np.asarray(image))
    y.append(file.split('/')[2].split('_')[0])

df = pd.DataFrame(data={'X': X, 'y': y})

np.set_printoptions(threshold=sys.maxsize)
df.to_csv('data/cats.csv', index=False, sep='\t')