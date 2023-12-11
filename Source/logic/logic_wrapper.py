# Logic_Wrapper.py
from logic.employee_logic import Employee_Logic
from logic.flight_logic import Flight_logic
from logic.location_logic import Location_Logic
from logic.plane_logic import Plane_Logic

class Logic_Wrapper:
    def __init__(self, data_wrapper):
        self.employee_logic = Employee_Logic(data_wrapper)
        self.flight_logic = Flight_logic(data_wrapper)
        self.location_logic = Location_Logic(data_wrapper)
        self.plane_logic = Plane_Logic(data_wrapper)

    #Employees
    def add_employee(self, employee):
        self.employee_logic.add_new_employee(employee)
    
    def get_all_employees(self):
        return self.employee_logic.get_all_employees()

    def get_employee_by_id(self, employee_id):
        return self.employee_logic.get_employee_by_id(employee_id)

    def is_employee_a_pilot(self, employee_id):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            return self.employee_logic.is_employee_a_pilot(employee)
        return False

    def update_employee_details(self, employee_id, new_details):
        self.employee_logic.update_employee_details(employee_id, new_details)

    def update_employee(self, id, new_data):
        self.employee_logic.update_employee(id, new_data)

    #Locations
    def add_location(self, id, country, airport_code, flight_duration, distance, manager_name, emergency_phone):
        self.location_logic.add_new_location(id, country, airport_code, flight_duration, distance, manager_name, emergency_phone)

    def get_all_locations(self):
        return self.location_logic.get_all_locations()
    
    def get_location_by_id(self, location_id):
        return self.location_logic.get_location_by_id(location_id)
    
    def update_location_details(self, location_id, new_details):
        self.location_logic.update_location_details(location_id, new_details)