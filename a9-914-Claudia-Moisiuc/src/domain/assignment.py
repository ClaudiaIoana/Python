class Assignment:
    def __init__(self, assignment_id, description, deadline):
        self.__assignment_id = assignment_id
        self.__description = description
        self.__deadline = deadline

    @property
    def id(self):
        return self.__assignment_id

    @property
    def description(self):
        return self.__description

    @property
    def deadline(self):
        return self.__deadline

    @id.setter
    def id(self, value):
        self.__assignment_id = value

    @description.setter
    def description(self, value):
        self.__description = value

    @deadline.setter
    def deadline(self, value):
        self.__deadline = value
