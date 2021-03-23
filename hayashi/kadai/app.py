from dataaccess import DataAccess
from Genetic_Algorithm import Genetic_Algorithm
import numpy as np

da = DataAccess()
# GA = Genetic_Algorithm()

spot_list = da.get_name_latitude_longitude()
a = np.array([])
for spot in spot_list:
    a = np.append(a,spot, axis=0)
a = a.reshape(5,3)
print(a)


spot_list = a[:,1:].astype(np.float)
GA = Genetic_Algorithm(len(spot_list), spot_list)
GA.main()
