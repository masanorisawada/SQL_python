# -*- coding: utf-8 -*-
from dataaccess import DataAccess
import numpy as np


#緯度、経度の順番
def space_calc(lon_p,lat_p,lon_q,lat_q):
    r = 6731
    theta_deruta = np.abs(lon_p - lon_q)
    theta_gamma = np.abs(lat_p - lat_q)


    r_lat_p=np.radians(lat_p)
    r_lon_p=np.radians(lon_q)
    r_lat_q=np.radians(lat_p)
    r_lon_q=np.radians(lon_q)

    px=np.arctan(np.tan(r_lat_p))
    qx=np.arctan(np.tan(r_lat_q))

    # theta = 2*np.arcsin(np.sqrt(np.sin(theta_deruta/2)**2 + np.cos(px) * np.cos(qx) * np.sin(theta_gamma/2)**2))
    theta = np.arccos(np.sin(px) * np.sin(qx) + np.cos(px) * np.cos(qx) * np.cos(theta_gamma))
    #地球の半径
    d = r * theta 
    return float(d)

# space_calc(139.7721169, 35.6254527, 134.2298797, 35.5417282)
def move_time():
    da = DataAccess()
    name_1 = input("距離計算の場所を一つ入力してください")
    name_2 = input("距離計算の場所を、もう一つ入力してください")
    spot_list = da.get_latitude_longitude(name_1)
    x = da.get_latitude_longitude(name_2)
    a = np.array([])
    b = np.array([])
    for spot,i in zip(spot_list,x):
        a = np.append(a,spot, axis=0)
        b = np.append(b,i,axis=0)
        
    move_time = space_calc(a[1],a[0],b[1],b[0]) 
    print(move_time/4.0)

