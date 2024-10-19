# app/controllers/StationController.py
from ..Model.Station import Station
from .. import db

class StationController:
    @staticmethod
    def create_station(data):
        new_station = Station(
            name=data['name'], 
            location=data['location'], 
            location_pad_img=data.get('location_pad_img')
        )
        db.session.add(new_station)
        db.session.commit()
        return new_station

    @staticmethod
    def get_station_by_id(station_id):
        return Station.query.get(station_id)

    @staticmethod
    def get_all_stations():
        return Station.query.all()

    @staticmethod
    def update_station(station_id, data):
        station = Station.query.get(station_id)
        if station:
            station.name = data.get('name', station.name)
            station.location = data.get('location', station.location)
            station.location_pad_img = data.get('location_pad_img', station.location_pad_img)
            db.session.commit()
            return station
        return None

    @staticmethod
    def delete_station(station_id):
        station = Station.query.get(station_id)
        if station:
            db.session.delete(station)
            db.session.commit()
            return True
        return False
