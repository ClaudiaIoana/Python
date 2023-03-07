class Student:
    def __init__(self, student_id, name, group):
        self.__student_id = student_id
        self.__name = name
        self.__group = group

    @property
    def id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    @id.setter
    def id(self, value):
        self.__student_id = value

    @name.setter
    def name(self, value):
        self.__name = value

    @group.setter
    def group(self, value):
        self.__group = value

