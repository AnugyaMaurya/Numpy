'''How to get values of an NumPy array at certain index positions'''

import numpy as np
  

a1 = np.array([11, 10, 22, 30, 33])
  
a2 = np.array([1, 15, 60])
  
print("\nTake 1 and 15 from Array 2 and put them in\
1st and 5th position of Array 1")
  
a1.put([0, 4], a2)
  
print("Resultant Array :")
print(a1)
