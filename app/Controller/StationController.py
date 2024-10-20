import os
from flask import current_app
from ..Model.Station import Station
from .. import db

class StationController:
    @staticmethod
    def create_station(data, image=None):
        new_station = Station(
            name=data['name'],
            location=data['location'],
            location_pad_img=image  # Store the image path if provided
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
    def update_station(station_id, data, image=None):
        station = Station.query.get(station_id)
        if station:
            station.name = data.get('name', station.name)
            station.location = data.get('location', station.location)

            if image:
                # Save and update the image if a new image is provided
                image_path = StationController.save_image(image)
                station.location_pad_img = image_path

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
