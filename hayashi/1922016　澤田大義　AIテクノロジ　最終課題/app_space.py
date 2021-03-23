from dataaccess import DataAccess
import numpy as np
from distance_movetime import space_calc

da = DataAccess()

#空間的計算（ユークリッド）
name = input("調べたい場所を入力してください")
space = da.get_spots_by_space(name)
space = np.array(space)
spot_list = da.get_space()
a = np.array([])
for spot in spot_list:
    a = np.append(a,spot, axis=0)
a = a.reshape(5,3)
print(a[1,1:])
print(space[0,0])
kekka = []
for item in a:
    # kekka.append([item[0], np.linalg.norm(item[1:].astype(np.float) - space.astype(np.float))])
    kekka.append([item[0], space_calc(item[1].astype(np.float), item[2].astype(np.float), space[0,0].astype(np.float), space[0,1].astype(np.float))])
print(kekka)