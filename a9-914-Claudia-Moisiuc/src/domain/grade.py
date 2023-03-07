class Grade:
    def __init__(self, assignment_id, student_id, grade_value):
        self.__assignment_id = assignment_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    @property
    def student_id(self):
        return self.__student_id

    @property
    def assign_id(self):
        return self.__assignment_id

    @property
    def grade(self):
        return self.__grade_value

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @assign_id.setter
    def assign_id(self, value):
        self.__assignment_id = value

    @grade.setter
    def grade(self, value):
        self.__grade_value = value
