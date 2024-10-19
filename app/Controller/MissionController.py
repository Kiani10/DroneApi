# app/controllers/MissionController.py
from ..Model.Mission import Mission
from ..Model.MissionCoordinates import MissionCoordinates
from .. import db

class MissionController:
    # Mission Functions
    @staticmethod
    def create_mission(data):
        new_mission = Mission(
            mission_datetime=data['mission_datetime'], 
            location_pad=data['location_pad'], 
            img=data.get('img'),
            drone_id=data['drone_id']
        )
        db.session.add(new_mission)
        db.session.commit()
        return new_mission

    @staticmethod
    def get_mission_by_id(mission_id):
        return Mission.query.get(mission_id)

    @staticmethod
    def get_all_missions():
        return Mission.query.all()

    @staticmethod
    def update_mission(mission_id, data):
        mission = Mission.query.get(mission_id)
        if mission:
            mission.mission_datetime = data.get('mission_datetime', mission.mission_datetime)
            mission.location_pad = data.get('location_pad', mission.location_pad)
            mission.img = data.get('img', mission.img)
            mission.drone_id = data.get('drone_id', mission.drone_id)
            db.session.commit()
            return mission
        return None

    @staticmethod
    def delete_mission(mission_id):
        mission = Mission.query.get(mission_id)
        if mission:
            db.session.delete(mission)
            db.session.commit()
            return True
        return False

    # Mission Coordinates Functions
    @staticmethod
    def create_mission_coordinates(data):
        new_coordinates = MissionCoordinates(
            mission_id=data['mission_id'], 
            latitude=data['latitude'], 
            longitude=data['longitude']
        )
        db.session.add(new_coordinates)
        db.session.commit()
        return new_coordinates

    @staticmethod
    def get_coordinates_by_mission_id(mission_id):
        return MissionCoordinates.query.filter_by(mission_id=mission_id).all()

    @staticmethod
    def update_mission_coordinates(coordinate_id, data):
        coordinates = MissionCoordinates.query.get(coordinate_id)
        if coordinates:
            coordinates.latitude = data.get('latitude', coordinates.latitude)
            coordinates.longitude = data.get('longitude', coordinates.longitude)
            db.session.commit()
            return coordinates
        return None

    @staticmethod
    def delete_mission_coordinates(coordinate_id):
        coordinates = MissionCoordinates.query.get(coordinate_id)
        if coordinates:
            db.session.delete(coordinates)
            db.session.commit()
            return True
        return False
