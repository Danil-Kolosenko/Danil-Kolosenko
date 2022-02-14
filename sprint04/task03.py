class Employee:
    def __init__(self, name: str, **kwargs):
        self.name = name.split()[0]
        self.lastname = name.split()[1]
        self.__dict__.update(kwargs)
