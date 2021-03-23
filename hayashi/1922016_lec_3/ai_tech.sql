CREATE TABLE data_spot_impr (
spot_id SERIAL PRIMARY KEY,
spot_area TEXT,
spot_name TEXT,
spot_latitude REAL,
spot_longitude REAL,
spot_elevation INTEGER,
spot_history_culture INTEGER,
spot_nature INTEGER,
spot_view INTEGER,
spot_opentime INTEGER,
spot_closetime INTEGER,
spot_recommend_time INTEGER
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime, spot_recommend_time
) VALUES (
'東京', '高尾山', 35.6254527, 139.7576692, 599,
0, 1, 1,
10, 16, 6
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime, spot_recommend_time
) VALUES (
'鳥取', '鳥取砂丘', 35.5417282, 134.2298797, 0,
0, 1, 1,
8, 17, 1
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime, spot_recommend_time
) VALUES (
'東京', '築地本願寺', 35.6676278, 139.7721169, 2,
1, 0, 1,
6, 16, 2
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime, spot_recommend_time
) VALUES (
'東京', '羽田空港', 35.5437833, 139.7663947, 11,
1, 0, 1,
0, 24, 4
);

INSERT INTO data_spot_impr (
spot_area, spot_name, spot_latitude, spot_longitude, spot_elevation,
spot_history_culture, spot_nature, spot_view,
spot_opentime, spot_closetime, spot_recommend_time
) VALUES (
'千葉', '東京ドイツ村', 35.4051649, 140.0603771, 60,
0, 1, 1,
10, 17, 5
);


