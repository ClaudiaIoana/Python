import random
import names

from src.domain.student import Student
from src.domain.validators import UniqueError


class StudentService:
    def __init__(self, repository):
        self.__repository = repository

    def unique(self, _id):
        """The function sees if the id is unique. """
        for ids in self.__repository.database.keys():
            if _id == self.__repository.__getitem__(ids):
                return False
        return True

    def verify_existence(self, _id):
        """Raises an error if the given id doesn't exist. """
        if self.unique(_id) is False:
            raise UniqueError("*This id doesn't exist.*")

    @property
    def database(self):
        """The function returns the student database. """
        return self.__repository.database

    def random_data(self):
        """The function adds random data for the 20 start up students. """
        for i in range(20):
            ok = False
            while ok is False:
                idr = int(random.randint(10, 99))
                ok = self.unique(idr)
            name = names.get_full_name()
            group = int(random.randint(100, 109))
            student = Student(idr, name, group)
            self.__repository.__add__(student)

    def add(self, idd, name, group):
        """The function adds a student if the id does not already exist. """
        if self.unique(idd) is False:
            raise UniqueError("*The id already exists**")
        else:
            stud = Student(idd, name, group)
            self.__repository.__add__(stud)

    def remove(self, idd):
        """The function removes a student if it exists. """
        self.verify_existence(idd)
        self.__repository.__delitem__(idd)

    def update(self, idd, new_nm=None, new_gr=None):
        """The function updates the data of a student with a given id. """
        self.verify_existence(idd)
        if new_nm and new_gr is not None:
            new = Student(idd, new_nm, new_gr)
        elif new_nm is None:
            nm = self.__repository[idd].name
            new = Student(idd, nm, new_gr)
        else:
            old = self.__repository[idd].group
            new = Student(idd, new_nm, old)
        self.__repository.__delitem__(idd)
        self.__repository.__setitem__(idd, new)

    def find_by_id(self, entity_id):
        if entity_id in self.__repository.database:
            return self.__repository.database[entity_id]
        return None

    def sort(self):
        self.__repository.sort_student()
