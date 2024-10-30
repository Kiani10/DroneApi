from flask import current_app
from ..Model.Mission import Mission
from ..Model.MissionCoordinates import MissionCoordinates
from .. import db
import os
from werkzeug.utils import secure_filename

class MissionController:
    @staticmethod
    def create_mission(data):
        try:
            # Create the mission object
            new_mission = Mission(
                mission_datetime=data['mission_datetime'],
                location_pad=data['location_pad'],
                img=data['img'],  # The image path is passed here
                status=data['status'],
                drone_id=data['drone_id']
            )
            db.session.add(new_mission)
            db.session.flush()  # To get the mission ID for coordinates

            # Add mission coordinates
            if 'coordinates' in data:
                for coord in data['coordinates']:
                    new_coordinates = MissionCoordinates(
                        mission_id=new_mission.id,
                        latitude=coord['latitude'],
                        longitude=coord['longitude']
                    )
                    db.session.add(new_coordinates)

            db.session.commit()  # Commit all changes
            return new_mission

        except Exception as e:
            db.session.rollback()  # Rollback if something fails
            raise e
    @staticmethod
    def get_mission_by_id(mission_id):
        return Mission.query.get(mission_id)

    @staticmethod
    def get_all_missions(DroneList):
        return Mission.query.filter(Mission.drone_id.in_(DroneList)).all()

    @staticmethod
    def update_mission(mission_id, status, data=None, file=None):
        # mission = Mission.query.get(mission_id)
        # if mission:
        #     mission.mission_datetime = data.get('mission_datetime', mission.mission_datetime)
        #     mission.status = data.get('status', mission.status)
        #     mission.location_pad = data.get('location_pad', mission.location_pad)
        #     mission.drone_id = data.get('drone_id', mission.drone_id)

        #     # Handle image file upload for update
        #     if file:
        #         if not MissionController.allowed_file(file.filename):
        #             raise ValueError("Invalid image format.")
        #         filename = secure_filename(file.filename)
        #         img_path = os.path.join(MissionController.UPLOAD_FOLDER, filename)
        #         file.save(os.path.join(current_app.root_path, img_path))
        #         mission.img = img_path  # Update image path if a new image is provided

        #     db.session.commit()
        #     return mission
        # return None
        mission = Mission.query.get(mission_id)
        if mission:
            if mission.status==1:
                mission.status=status
                db.session.commit()
                return True
        return False

    @staticmethod
    def delete_mission(mission_id):
        mission = Mission.query.get(mission_id)
        if mission:
            db.session.delete(mission)
            db.session.commit()
            return True
        return False

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
    def delete_mission_coordinates(mission_id):
        coordinates = MissionCoordinates.query.filter_by(mission_id=mission_id).all()  # Query all coordinates with the given mission_id
        if coordinates:
            for coord in coordinates:
                db.session.delete(coord)
            db.session.commit()
            return True
        return False


        