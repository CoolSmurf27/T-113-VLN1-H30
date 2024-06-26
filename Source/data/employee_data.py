#employee_data.py
import csv
from model.employee_model import Employee

class Employee_Data:
    def __init__(self) -> None:
        self.model = "files/employees.csv"
        self.fieldname = [
            "id", 
            "name", 
            "address", 
            "cell_phone", 
            "email", 
            "title", 
            "home_phone", 
            "plane_licenses"]

    def employee_constructor(self):
        employee_list = []
        with open(self.model, newline='', encoding="utf-8") as file:
            dict_file = csv.DictReader(file)
            for row in dict_file:
                if row["plane_licenses"] == "None":
                    licenses="None"
                else:
                    licenses= [x for x in row["plane_licenses"].split(":")]                    
                employee_list.append(Employee(
                    row["id"], 
                    row["name"], 
                    row["address"], 
                    row["cell_phone"], 
                    row["email"], 
                    row["title"], 
                    row["home_phone"], 
                    licenses))
        return employee_list

    def add_employee_data(self, employee):
        with open(self.model, 'a', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)  
            if file.tell() == 0:  
                dict_write.writeheader()
            dict_write.writerow({
                "id": employee.id, 
                "name": employee.name, 
                "address": employee.address, 
                "cell_phone": employee.cell_phone, 
                "email": employee.email, 
                "title": employee.title, 
                "home_phone": employee.home_phone, 
                "plane_licenses": employee.plane_licenses})

    def get_employee_by_id(self, id):
        all_employees = self.employee_constructor()
        for employee in all_employees:
            if employee.id == id:
                return employee
        return None
    
    def modify_employee_data(self, updated_employee_list):
        with open(self.model, 'w', newline='', encoding="utf-8") as file:
            dict_write = csv.DictWriter(file, fieldnames=self.fieldname)
            dict_write.writeheader()
            for employee in updated_employee_list:
                # Format plane licenses as a colon-separated string
                if isinstance(employee.plane_licenses, list):
                    formatted_licenses = ":".join(employee.plane_licenses)
                else:
                    formatted_licenses = employee.plane_licenses

                dict_write.writerow({
                    "id": employee.id, 
                    "name": employee.name, 
                    "address": employee.address, 
                    "cell_phone": employee.cell_phone, 
                    "email": employee.email, 
                    "title": employee.title, 
                    "home_phone": employee.home_phone, 
                    "plane_licenses": formatted_licenses  # Save the formatted licenses
                })


    
