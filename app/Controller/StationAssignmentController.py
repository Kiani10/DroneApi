# app/controllers/StationAssignmentController.py
from ..Model.StationDroneRecord import StationDroneRecord
from ..Model.StationOperatorRecord import StationOperatorRecord
from .. import db

class StationAssignmentController:
    # Functions for Station Drone Record
    @staticmethod
    def create_station_drone_record(data):
        new_record = StationDroneRecord(
            drone_id=data['drone_id'], 
            station_id=data['station_id']
        )
        db.session.add(new_record)
        db.session.commit()
        return new_record

    @staticmethod
    def get_station_drone_record_by_id(record_id):
        return StationDroneRecord.query.get(record_id)

    @staticmethod
    def get_all_station_drone_records():
        return StationDroneRecord.query.all()

    @staticmethod
    def update_station_drone_record(record_id, data):
        record = StationDroneRecord.query.get(record_id)
        if record:
            record.drone_id = data.get('drone_id', record.drone_id)
            record.station_id = data.get('station_id', record.station_id)
            db.session.commit()
            return record
        return None

    @staticmethod
    def delete_station_drone_record(record_id):
        record = StationDroneRecord.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False

    # Functions for Station Operator Record
    @staticmethod
    def create_station_operator_record(data):
        new_record = StationOperatorRecord(
            operator_id=data['operator_id'], 
            station_id=data['station_id']
        )
        db.session.add(new_record)
        db.session.commit()
        return new_record

    @staticmethod
    def get_station_operator_record_by_id(record_id):
        return StationOperatorRecord.query.get(record_id)

    @staticmethod
    def get_all_station_operator_records():
        return StationOperatorRecord.query.all()

    @staticmethod
    def update_station_operator_record(record_id, data):
        record = StationOperatorRecord.query.get(record_id)
        if record:
            record.operator_id = data.get('operator_id', record.operator_id)
            record.station_id = data.get('station_id', record.station_id)
            db.session.commit()
            return record
        return None

    @staticmethod
    def delete_station_operator_record(record_id):
        record = StationOperatorRecord.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False
