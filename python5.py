'''Change data type of given numpy array'''

import numpy as np
  
# Create a numpy array
arr = np.array([10, 20, 30, 40, 50])

# change the dtype to 'float64'
arr = arr.astype('float64')
print(arr.dtype)
