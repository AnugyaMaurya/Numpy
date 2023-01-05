'''convert array to uppercase'''

import numpy as np
  
  
in_arr = np.array(['geeks', 'for', 'geeks'])
  
print ("input array : ", in_arr)
  
out_arr = np.char.upper(in_arr)
print ("output uppercased array :", out_arr )
