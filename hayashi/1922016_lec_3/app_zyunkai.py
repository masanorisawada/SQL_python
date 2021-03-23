from dataaccess import DataAccess
import numpy as np

da = DataAccess()
x = da.get_distance()
a = np.array([])
for i in x:
    a = np.append(a,i,axis=0)
a = a.reshape(5,3)
print(a)
