import numpy as np
# DataTypes & Attribute
#NumPy's main datatype is ndarray
al = np.array([1,2,3])
type(al)
a2 = np.array([[1,2.0, 3.3],
               [4, 5, 6.5]])
a3 = np.array([[[1 , 2, 3],
                [4, 5, 6], 
                 [7, 8,9]],
                [[10, 11, 12],
                 [13,14,15],
                  [ 16, 17, 18]]
               ])
a2.size
a2.shape,a3.shape, 
a2.ndim, a3.ndim 

import pandas as pd
df = pd.DataFrame(a2)
df

sample_array = np.array([1,2,3])
sample_array

range_array = np.arange(0,10,2)
range_array

random_array = np.random.randint(0, 10, size=(3, 5))
random_array

np.random.random((5,3))

random_array_2=np.random.random((5,3))
random_array_2
random_array_3 = np.random.rand(5, 3)
random_array_3