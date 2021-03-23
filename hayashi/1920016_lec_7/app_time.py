from dataaccess import DataAccess
import numpy as np

da = DataAccess()

#時間的計算（内積）
name = input("調べたい場所を入力してください")
time = da.get_spots_by_time(name)
time = np.array(time)
spot_list = da.get_time()
a = np.array([])
for spot in spot_list:
    a = np.append(a,spot, axis=0)
a = a.reshape(3,3)
kekka = []
for item in a:
    kekka.append([item[0], np.sum(item[1:].astype(np.float) * time.astype(np.float))])
print(kekka)
