from dataaccess import DataAccess
import numpy as np

da = DataAccess()

#意味的計算（内積）
spot_list = da.get_impression()
print(spot_list)
a = np.array([])
for spot in spot_list:
    a = np.append(a,spot, axis=0)
a = a.reshape(5,4)
c = 3
b = np.zeros(c)
print(b)
x = input("その場所に歴史がありますか？（あればはいでなければいいえ）")
if x == "はい":
    b[0] = 1
y = input("その場所に自然がありますか？（あればはいでなければいいえ）")
if y == "はい":
    b[1] = 1
z = input("その場所に景観がありますか？（あればはいでなければいいえ）")
if z == "はい":
    b[2] = 1
kekka = []
for item in a:
    kekka.append([item[0], np.sum(item[1:].astype(np.int) * b)])
kekka.sort(reverse=True)
print(kekka)












