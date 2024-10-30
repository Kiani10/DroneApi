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
    email = data.get('email')
    password = data.get('passwrd')
    print(email)
    # Check if the user exists by name
    user = Login.query.filter_by(email=email).first()
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

@main.route('/drones/specific/<int:operator_id>', methods=['GET'])
def get_specific_drones(operator_id):
        #print(operator_id)
    #first we have to search that any station is assigned to that operator
    StationOperatorList=StationAssignmentController.get_station_operator_records_by_id(operator_id)
    #print(StationOperatorList)
    #Second we have to see if any drone is assigned to that station
    DroneList=[]
    for station in StationOperatorList:
        station=station.to_dict()
        #So we will get statoin id from there
        StationDroneRecord=StationAssignmentController.get_station_drone_records_by_id(station['station_id'])
        #print(StationDroneRecord)
        for drone in StationDroneRecord:
            DroneList.append(drone.drone_id)
        
    print(DroneList)
    drones = DroneController.get_all_drones()
    return jsonify([drone.to_dict() for drone in drones if drone.id in DroneList])



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
@main.route('/missions/<int:operator_id>', methods=['GET'])
def get_missions(operator_id):
    #print(operator_id)
    #first we have to search that any station is assigned to that operator
    StationOperatorList=StationAssignmentController.get_station_operator_records_by_id(operator_id)
    #print(StationOperatorList)
    #Second we have to see if any drone is assigned to that station
    DroneList=[]
    for station in StationOperatorList:
        station=station.to_dict()
        #So we will get statoin id from there
        StationDroneRecord=StationAssignmentController.get_station_drone_records_by_id(station['station_id'])
        #print(StationDroneRecord)
        for drone in StationDroneRecord:
            DroneList.append(drone.drone_id)
        
    print(DroneList)

    #Third we have to give only list of those mission where drone is assigned
    

    missions = MissionController.get_all_missions(DroneList)

    print(missions)
    return jsonify([mission.to_dict() for mission in missions])

@main.route('/mission/<int:mission_id>', methods=['GET'])
def get_mission(mission_id):
    mission = MissionController.get_mission_by_id(mission_id)
    if mission:
        return jsonify(mission.to_dict())
    return jsonify({'message': 'Mission not found'}), 404

UPLOAD_FOLDER_MISSION = 'upload/missionHelipadImages/'

@main.route('/mission', methods=['POST'])
def create_mission():
    try:
        # Ensure mission_datetime, location_pad, drone_id are present in the form data
        mission_datetime = request.form.get('mission_datetime')
        location_pad = request.form.get('location_pad')
        status=request.form.get('status')
        drone_id = request.form.get('drone_id')
        
        # Ensure the required fields are provided
        if not mission_datetime or not location_pad or not drone_id:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Process the coordinates from the form data
        coordinates = []
        i = 0
        while True:
            lat = request.form.get(f'coordinates[{i}][latitude]')
            lng = request.form.get(f'coordinates[{i}][longitude]')
            if lat and lng:
                coordinates.append({
                    'latitude': float(lat),
                    'longitude': float(lng)
                })
                i += 1
            else:
                break
        
        # At least two coordinates must be provided
        if len(coordinates) < 2:
            return jsonify({'error': 'At least two coordinates are required'}), 400
        
        # Handle image upload
        image = request.files.get('img')
        if image:
            # Ensure the upload directory exists
            if not os.path.exists(UPLOAD_FOLDER_MISSION):
                os.makedirs(UPLOAD_FOLDER_MISSION)
            
            # Secure the image filename and save it
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER_MISSION, filename)
            image.save(image_path)
        else:
            return jsonify({'error': 'Image is required'}), 400

        # Prepare mission data to pass to the controller
        mission_data = {
            'mission_datetime': mission_datetime,
            'location_pad': location_pad,
            'img': image_path,  # Save the image path to the database
            'status':status,
            'drone_id': int(drone_id),
            'coordinates': coordinates
        }

        # Create the mission through the controller
        new_mission = MissionController.create_mission(mission_data)
        
        return jsonify(new_mission.to_dict()), 201

    except Exception as e:
        print(e)
        return jsonify({'error': 'Something went wrong during mission creation'}), 500

@main.route('/mission/<int:mission_id>', methods=['PUT'])
def update_mission(mission_id):
    # try:
    #     data = request.form.to_dict()
    #     file = request.files.get('image')  # Get the uploaded image file
    #     updated_mission = MissionController.update_mission(mission_id, data, file)
    #     if updated_mission:
    #         return jsonify(updated_mission.to_dict())
    #     return jsonify({'message': 'Mission not found'}), 404
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 400
    data = request.get_json()
    res=MissionController.update_mission(mission_id,data['status'])
    if res:
          print('Updated')
          return jsonify({'message': 'Mission  Status Updated Successfulluy'}) 
    print('Updated')
    return jsonify({'message': 'Mission not Updated'}), 404


    

@main.route('/mission/<int:mission_id>', methods=['DELETE'])
def delete_mission(mission_id):

    # first getting the path so we can also delete the image of mission from the server
    mission = MissionController.get_mission_by_id(mission_id)
    mission=mission.to_dict()
    path=mission['img']

    #but first we have to delete misson coordinates then we can delete mission
    MissionController.delete_mission_coordinates(mission_id)

    #then we will delete the mission
    if MissionController.delete_mission(mission_id):
        if os.path.exists(path):
            try:
                os.remove(path)  # Remove the old image
            except OSError as e:
                print(f"Error deleting file: {e}")
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

@main.route('/station/<int:station_id>', methods=['SGET'])
def get_station(station_id):
    station = StationController.get_station_by_id(station_id)
    if station:
        return jsonify(station.to_dict())
    return jsonify({'message': 'Station not found'}), 404

UPLOAD_FOLDER = 'upload/'  # Define where you want to save the uploaded files

@main.route('/station', methods=['POST'])
def create_station():
    if not os.path.exists(UPLOAD_FOLDER):
      os.makedirs(UPLOAD_FOLDER)
    if 'station_name' not in request.form or 'latitude' not in request.form or 'longitude' not in request.form:
        return jsonify({'message': 'Missing required fields'}), 400
    # Ensure the upload folder exists

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


################################################################################
@main.route('/station/<int:station_id>', methods=['PUT'])
def update_station(station_id):
    # Fetch the station from the database
    existing_station = StationController.get_station_by_id(station_id)

    if not existing_station:
        return jsonify({'message': 'Station not found'}), 404

    # Get form data for name, latitude, and longitude
    station_name = request.form.get('station_name')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    print(latitude,longitude,station_name)
    # Ensure latitude and longitude are not None
    if not latitude or not longitude:
        return jsonify({'message': 'Latitude or Longitude is missing'}), 400

    # Prepare data for updating the station
    data = {
        'name': station_name,
        'location': f'{latitude},{longitude}',  # Concatenate latitude and longitude
    }

    # Handle image file if provided
    image = request.files.get('location_pad_img', None)  # Fetch image if present

    # If a new image is provided, handle old image deletion and save the new one
    
    if image:
        if existing_station.location_pad_img:  # If an old image exists, delete it
            old_image_path = existing_station.location_pad_img
            if os.path.exists(old_image_path):
                try:
                    os.remove(old_image_path)  # Remove the old image
                except OSError as e:
                    print(f"Error deleting file: {e}")

        # Save the new image and update the image path in the database
        new_image_path = save_image(image)
        print(new_image_path)
        data['location_pad_img'] = new_image_path  # Add the new image path to the data
        updated_station = StationController.update_station(station_id, data,image)

    # Call the controller to update the station with the new data
    if not image:
        updated_station = StationController.update_station(station_id, data)
        

    if updated_station:
        return jsonify(updated_station.to_dict()), 200
    return jsonify({'message': 'Station not found'}), 404


def save_image(image):
    # Ensure the folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # Generate a secure filename
    filename = secure_filename(image.filename)
    
    # Define the full path for the image
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    
    # Save the image
    image.save(image_path)
    
    return image_path  # Return the path where the image is stored
################################################################################


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
    print(data)
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
