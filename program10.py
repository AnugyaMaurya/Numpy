
# Python code to demonstrate to replace negative value with 0
import numpy as np
 
ini_array1 = np.array([1, 2, -3, 4, -5, -6])
ini_array1[ini_array1<0] = 0
print("New resulting array: ", ini_array1)
