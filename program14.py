'''find mean,variance,standard deviation'''

import numpy as np
          

gfg = np.matrix('[64, 1; 12, 3]')
          

g = gfg.mean()
    
print(g)
print("var of arr : ", np.var(gfg)) 
print("std of arr : ", np.std(arr))
