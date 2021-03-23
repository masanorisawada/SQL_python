from dataaccess import DataAccess
from Genetic_Algorithm import Genetic_Algorithm
import numpy as np

da = DataAccess()
# GA = Genetic_Algorithm()

# spot_list = da.get_name_latitude_longitude()
# a = np.array([])
# for spot in spot_list:
#     a = np.append(a,spot, axis=0)
# a = a.reshape(5,3)
# print(a[:,0])

space = np.array([])
name_x = input("調べたい場所を入力してください")
space_x = da.get_spots_by_space_name(name_x)
space = np.append(space,space_x)
name_y = input("調べたい場所を入力してください")
space_y = da.get_spots_by_space_name(name_y)
space = np.append(space,space_y)
name_z = input("調べたい場所を入力してください")
space_z = da.get_spots_by_space_name(name_z)
space = np.append(space,space_z)
space = space.reshape(3,3)
print(space)
# a = np.array([])
# for spot in space:
#     a = np.append(a,spot, axis=0)
# a = a.reshape(3,3)
# kekka = []
# for item in a:
#     kekka.append([item[0], np.sum(item[1:].astype(np.float) * time.astype(np.float))])
# print(kekka)

spot_name = space[:,0]
spot_list = space[:,1:].astype(np.float)
GA = Genetic_Algorithm(len(spot_list), spot_list, spot_name)
GA.main()