'''use geometric()function'''

import numpy as np
import matplotlib.pyplot as plt
  

gfg = np.random.geometric(0.65, 1000)
  
count, bins, ignored = plt.hist(gfg, 40, density = True)
plt.show()
