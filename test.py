import numpy as np
import matplotlib.pyplot as plt
from imglib import *
from arraytoimg import *

from sorting import *

arr = []

for i in range(1,30):
    arr.append(i)

import random
random.shuffle(arr)

"""
image = getimg(arr)

plt.imshow(image)
plt.show()

print(arr)
"""

heap_sort(arr, "exports/")