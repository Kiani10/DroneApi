# app/controllers/DroneController.py
from ..Model.Drone import Drone
from .. import db

class DroneController:
    @staticmethod
    def create_drone(data):
        new_drone = Drone(
            name=data['name'], 
            ceiling=data['ceiling'], 
            speed=data['speed'], 
            battery=data['battery'], 
            payload=data['payload']
        )
        db.session.add(new_drone)
        db.session.commit()
        return new_drone

    @staticmethod
    def get_drone_by_id(drone_id):
        return Drone.query.get(drone_id)

    @staticmethod
    def get_all_drones():
        return Drone.query.all()

    @staticmethod
    def update_drone(drone_id, data):
        drone = Drone.query.get(drone_id)
        if drone:
            drone.name = data.get('name', drone.name)
            drone.ceiling = data.get('ceiling', drone.ceiling)
            drone.speed = data.get('speed', drone.speed)
            drone.battery = data.get('battery', drone.battery)
            drone.payload = data.get('payload', drone.payload)
            db.session.commit()
            return drone
        return None

    @staticmethod
    def delete_drone(drone_id):
        drone = Drone.query.get(drone_id)
        if drone:
            db.session.delete(drone)
            db.session.commit()
            return True
        return False
