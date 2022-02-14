class Employee:
    def __init__(self, first_name, last_name, salary):
        self.firstname = first_name
        self.lastname = last_name
        self.salary = salary

    @classmethod
    def from_string(cls, str):
        return cls(str.split('-')[0], str.split('-')[1], int(str.split('-')[2]))
