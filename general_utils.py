import pandas as pd
from geopy.distance import geodesic
from importlib import reload

#Local Modules


class GeneralUtls:
    """ local utils class contains common functions that can be used across
        many different programs
    """

    @staticmethod
    def parse_dates(str_date, format=None):
        if format is None:
            format = '%Y-%m-%dT%H:%M:%S'
        return pd.to_datetime(str_date, format=format)

    @staticmethod
    def get_geo_distance(lon1, lat1, lon2, lat2):
        point1 = (lat1,lon1)
        point2 = (lat2,lon2)
        return geodesic(point1, point2).m

    @staticmethod
    def substract_days_from_date(str_date,ndays):
        _dt = GeneralUtls.parse_dates(str_date)
        _dt2 = _dt - pd.Timedelta(days=ndays)
        return _dt2.strftime('%Y-%m-%d')

    @staticmethod
    def add_days_to_date(str_date, ndays):
        _dt = GeneralUtls.parse_dates(str_date)
        _dt2 = _dt + pd.Timedelta(days=ndays)
        return _dt2.strftime('%Y-%m-%d')

    @staticmethod
    def reload(_module):
            _module = reload(_module)



if __name__== "__main__":
    import datetime
    print(GeneralUtls.parse_dates(datetime.datetime.now()))
    print(GeneralUtls.substract_days_from_date('2019-04-20',55))
    print(GeneralUtls.add_days_to_date('2019-04-20', 55))