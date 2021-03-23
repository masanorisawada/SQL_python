from var import Var
from db import DB
class DataAccess:
    def get_impression(self):
        query = "SELECT spot_name, spot_history_culture, spot_nature, spot_view FROM data_spot_impr"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
    def get_space(self):
        query = "SELECT spot_name, spot_latitude, spot_longitude, spot_elevation FROM data_spot_impr"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
    def get_time(self):
        query = "SELECT  spot_name, spot_opentime, spot_closetime FROM data_spot_impr "
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
    def get_spots_by_space(self, spot_name):
        query = "SELECT  spot_latitude, spot_longitude, spot_elevation FROM data_spot_impr WHERE spot_name = %s "
        data = (str(spot_name), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
    def get_spots_by_time(self, spot_name):
        query = "SELECT  spot_opentime, spot_closetime FROM data_spot_impr WHERE spot_name = %s "
        data = (str(spot_name), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
    def get_latitude_longitude(self, spot_name):
        query = "SELECT  spot_latitude, spot_longitude FROM data_spot_impr WHERE spot_name = %s "
        data = (str(spot_name), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)
    def get_distance(self):
        query = "SELECT  spot_name, spot_latitude, spot_longitude FROM data_spot_impr"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

