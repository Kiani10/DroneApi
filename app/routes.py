# app/routes.py
import os
from flask import Blueprint, request, jsonify
from app.Controller.UserController import UserController
from app.Controller.DroneController import DroneController
from app.Controller.MissionController import MissionController
from app.Controller.StationController import StationController
from app.Controller.StationAssignmentController import StationAssignmentController
from app.Model.Login import Login
from werkzeug.utils import secure_filename


# Initialize a Blueprint
main = Blueprint('main', __name__)
# ==========================
# User Routes (Login, Admin, Operator)
# ==========================cls
@main.route('/user/login', methods=['POST'])
def login_user():
    # Extract the name and password from the request body
    data = request.get_json()
    name = data.get('name')
    password = data.get('passwrd')

    # Check if the user exists by name
    user = Login.query.filter_by(name=name).first()
    # Validate the password (assuming no hashing for now)
    if user and user.passwrd == password:
        # If credentials are valid, return a success response
        return jsonify({
            'message': 'Login successful',
            'user': user.to_dict()
        }), 200
    else:
        # If login fails, return an error
        return jsonify({'message': 'Invalid name or password'}), 401

@main.route('/users', methods=['GET'])
def get_users():
    users = UserController.get_all_users()
    return jsonify([user.to_dict() for user in users])

@main.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserController.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'message': 'User not found'}), 404

@main.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = UserController.create_user(data)
    return jsonify(new_user.to_dict()), 201

@main.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    updated_user = UserController.update_user(user_id, data)
    if updated_user:
        return jsonify(updated_user.to_dict())
    return jsonify({'message': 'User not found'}), 404

@main.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if UserController.delete_user(user_id):
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

# ==========================
# Operator Routes
# ==========================
@main.route('/operators', methods=['GET'])
def get_operators():
    operators = UserController.get_all_operators()
    return jsonify([operator.to_dict() for operator in operators])

@main.route('/operator/<int:operator_id>', methods=['GET'])
def get_operator(operator_id):
    operator = UserController.get_operator_by_id(operator_id)
    if operator:
        return jsonify(operator.to_dict())
    return jsonify({'message': 'Operator not found'}), 404

@main.route('/operator', methods=['POST'])
def create_operator():
    data = request.get_json()
    new_operator = UserController.create_operator(data)
    return jsonify(new_operator.to_dict()), 201

@main.route('/operator/<int:operator_id>', methods=['PUT'])
def update_operator(operator_id):
    data = request.get_json()
    updated_operator = UserController.update_operator(operator_id, data)
    if updated_operator:
        return jsonify(updated_operator.to_dict())
    return jsonify({'message': 'Operator not found'}), 404

@main.route('/operator/<int:operator_id>', methods=['DELETE'])
def delete_operator(operator_id):
    if UserController.delete_operator(operator_id):
        return jsonify({'message': 'Operator deleted successfully'})
    return jsonify({'message': 'Operator not found'}), 404

# ==========================
# Drone Routes
# ==========================
@main.route('/drones', methods=['GET'])
def get_drones():
    drones = DroneController.get_all_drones()
    return jsonify([drone.to_dict() for drone in drones])

@main.route('/drone/<int:drone_id>', methods=['GET'])
def get_drone(drone_id):
    drone = DroneController.get_drone_by_id(drone_id)
    if drone:
        return jsonify(drone.to_dict())
    return jsonify({'message': 'Drone not found'}), 404

@main.route('/drone', methods=['POST'])
def create_drone():
    data = request.get_json()
    new_drone = DroneController.create_drone(data)
    return jsonify(new_drone.to_dict()), 201

@main.route('/drone/<int:drone_id>', methods=['PUT'])
def update_drone(drone_id):
    data = request.get_json()
    updated_drone = DroneController.update_drone(drone_id, data)
    if updated_drone:
        return jsonify(updated_drone.to_dict())
    return jsonify({'message': 'Drone not found'}), 404

@main.route('/drone/<int:drone_id>', methods=['DELETE'])
def delete_drone(drone_id):
    if DroneController.delete_drone(drone_id):
        return jsonify({'message': 'Drone deleted successfully'})
    return jsonify({'message': 'Drone not found'}), 404

# ==========================
# Mission Routes
# ==========================
@main.route('/missions', methods=['GET'])
def get_missions():
    missions = MissionController.get_all_missions()
    return jsonify([mission.to_dict() for mission in missions])

@main.route('/mission/<int:mission_id>', methods=['GET'])
def get_mission(mission_id):
    mission = MissionController.get_mission_by_id(mission_id)
    if mission:
        return jsonify(mission.to_dict())
    return jsonify({'message': 'Mission not found'}), 404

@main.route('/mission', methods=['POST'])
def create_mission():
    data = request.get_json()
    new_mission = MissionController.create_mission(data)
    return jsonify(new_mission.to_dict()), 201

@main.route('/mission/<int:mission_id>', methods=['PUT'])
def update_mission(mission_id):
    data = request.get_json()
    updated_mission = MissionController.update_mission(mission_id, data)
    if updated_mission:
        return jsonify(updated_mission.to_dict())
    return jsonify({'message': 'Mission not found'}), 404

@main.route('/mission/<int:mission_id>', methods=['DELETE'])
def delete_mission(mission_id):
    if MissionController.delete_mission(mission_id):
        return jsonify({'message': 'Mission deleted successfully'})
    return jsonify({'message': 'Mission not found'}), 404

# Mission Coordinates routes (nested under missions)
@main.route('/mission/<int:mission_id>/coordinates', methods=['GET'])
def get_mission_coordinates(mission_id):
    coordinates = MissionController.get_coordinates_by_mission_id(mission_id)
    return jsonify([coord.to_dict() for coord in coordinates])

@main.route('/mission/<int:mission_id>/coordinate', methods=['POST'])
def create_mission_coordinates(mission_id):
    data = request.get_json()
    data['mission_id'] = mission_id  # Attach mission ID to the request data
    new_coordinates = MissionController.create_mission_coordinates(data)
    return jsonify(new_coordinates.to_dict()), 201

# ==========================
# Station Routes
# ==========================
@main.route('/stations', methods=['GET'])
def get_stations():
    stations = StationController.get_all_stations()
    return jsonify([station.to_dict() for station in stations])

@main.route('/station/<int:station_id>', methods=['GET'])
def get_station(station_id):
    station = StationController.get_station_by_id(station_id)
    if station:
        return jsonify(station.to_dict())
    return jsonify({'message': 'Station not found'}), 404

UPLOAD_FOLDER = 'uploads/'  # Define where you want to save the uploaded files

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@main.route('/station', methods=['POST'])
def create_station():
    if 'station_name' not in request.form or 'latitude' not in request.form or 'longitude' not in request.form:
        return jsonify({'message': 'Missing required fields'}), 400

    # Extract form fields
    station_name = request.form['station_name']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    # Check if an image file is part of the request
    if 'image' not in request.files:
        return jsonify({'message': 'No image file uploaded'}), 400

    # Save the image file
    image = request.files['image']
    filename = secure_filename(image.filename)
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)

    # Optionally, save the station data to the database
    new_station = {
        'name': station_name,
        'location': latitude+','+longitude,
        'image_path': image_path
    }
    StationController.create_station(new_station,image_path)
    print(new_station)

    # Return a success response
    return jsonify({'message': 'Station created successfully', 'station': new_station}), 201

@main.route('/station/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    # Handle image file if provided
    if 'location_pad_img' in request.files:
        image = request.files['location_pad_img']
    else:
        image = None

    data = {
        'name': request.form.get('name'),
        'location': request.form.get('location')
    }

    updated_station = StationController.update_station(station_id, data, image=image)
    if updated_station:
        return jsonify(updated_station.to_dict())
    return jsonify({'message': 'Station not found'}), 404

@main.route('/station/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    if StationController.delete_station(station_id):
        return jsonify({'message': 'Station deleted successfully'})
    return jsonify({'message': 'Station not found'}), 404

# ==========================
# Station Assignment Routes (Drones and Operators)
# ==========================
@main.route('/station_assignments/drones', methods=['GET'])
def get_station_drone_records():
    records = StationAssignmentController.get_all_station_drone_records()
    return jsonify([record.to_dict() for record in records])

@main.route('/station_assignments/drone/<int:record_id>', methods=['GET'])
def get_station_drone_record(record_id):
    record = StationAssignmentController.get_station_drone_record_by_id(record_id)
    if record:
        return jsonify(record.to_dict())
    return jsonify({'message': 'Station drone assignment not found'}), 404

@main.route('/station_assignments/drone', methods=['POST'])
def create_station_drone_record():
    data = request.get_json()
    new_record = StationAssignmentController.create_station_drone_record(data)
    return jsonify(new_record.to_dict()), 201

@main.route('/station_assignments/drone/<int:record_id>', methods=['PUT'])
def update_station_drone_record(record_id):
    data = request.get_json()
    updated_record = StationAssignmentController.update_station_drone_record(record_id, data)
    if updated_record:
        return jsonify(updated_record.to_dict())
    return jsonify({'message': 'Station drone assignment not found'}), 404

@main.route('/station_assignments/drone/<int:record_id>', methods=['DELETE'])
def delete_station_drone_record(record_id):
    if StationAssignmentController.delete_station_drone_record(record_id):
        return jsonify({'message': 'Station drone assignment deleted successfully'})
    return jsonify({'message': 'Station drone assignment not found'}), 404

@main.route('/station_assignments/operators', methods=['GET'])
def get_station_operator_records():
    records = StationAssignmentController.get_all_station_operator_records()
    return jsonify([record.to_dict() for record in records])

@main.route('/station_assignments/operator/<int:record_id>', methods=['GET'])
def get_station_operator_record(record_id):
    record = StationAssignmentController.get_station_operator_record_by_id(record_id)
    if record:
        return jsonify(record.to_dict())
    return jsonify({'message': 'Station operator assignment not found'}), 404

@main.route('/station_assignments/operator', methods=['POST'])
def create_station_operator_record():
    data = request.get_json()
    new_record = StationAssignmentController.create_station_operator_record(data)
    return jsonify(new_record.to_dict()), 201

@main.route('/station_assignments/operator/<int:record_id>', methods=['PUT'])
def update_station_operator_record(record_id):
    data = request.get_json()
    updated_record = StationAssignmentController.update_station_operator_record(record_id, data)
    if updated_record:
        return jsonify(updated_record.to_dict())
    return jsonify({'message': 'Station operator assignment not found'}), 404

@main.route('/station_assignments/operator/<int:record_id>', methods=['DELETE'])
def delete_station_operator_record(record_id):
    if StationAssignmentController.delete_station_operator_record(record_id):
        return jsonify({'message': 'Station operator assignment deleted successfully'})
    return jsonify({'message': 'Station operator assignment not found'}), 404
