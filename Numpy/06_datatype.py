#DATA TYPES
import numpy as np
a = np.array([1,2,3,4,5])                #int64
print("data type: ", a.dtype)

import numpy as np
b = np.array([1.0,2.1,3.2,4.4,5.5])      #float64
print("data type: ", b.dtype)

#simillarly for string and mixture of both

#you can also change the data type
a = np.array([1,2,3,4,5],dtype = np.int8)                # converting int64 to int8 
print("data type: ", a.dtype)
