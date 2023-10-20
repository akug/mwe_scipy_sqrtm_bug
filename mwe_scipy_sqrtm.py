import numpy as np
from scipy.linalg import sqrtm

data = np.load("./sample_sqrtm_fails.npz")["array"]
out, error = sqrtm(data, disp=False)
print(error)
# error in 1.11.2 and 1.11.3 is about 2.3e+24, but in 1.11.1 is 2.1e-28