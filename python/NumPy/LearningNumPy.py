# Key Technical Terms (MEMORIZE)

# ndarray

# Vectorization

# Broadcasting

# Shape

# Axis

# Dtype

# Homogeneous data

# Memory efficient

# C-backed operations

import numpy as np
arr = np.array([1, 2, 3])
arr * 2     # ✅ [2 4 6]

arr = np.array([1, 2, 3])
arr + np.array([4, 5, 6])  # ✅ [5 7 9]
print(arr.shape)  # ✅ (3,)