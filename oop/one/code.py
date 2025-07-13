class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def get_details(self):
        return {"Id": self.emp_id, "Name": self.name}

class Developer(Employee):
    def __init__(self, emp_id, name, programming_language):
        super().__init__(emp_id, name)
        self.programming_language = programming_language

    def get_details(self):
        ret = super().get_details()
        ret.update({"Programming Language": self.programming_language})
        return ret

class Manager(Employee):
    def __init__(self, emp_id, name, team_size):
        super().__init__(emp_id, name)
        self.team_size = team_size

    def get_details(self):
        ret = super().get_details()
        ret.update({"Team Size": self.team_size})
        return ret

print("Employee  >> ", Employee(47,"Salma").get_details())
print("Developer >> ", Developer(39,"Karim","Scala").get_details())
print("Manager   >> ", Manager(1,"Alaa",8).get_details())
