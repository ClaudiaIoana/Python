import unittest

from src.domain.student import Student
from src.repository.repository import Repository
from src.services.student_services import StudentService


class StudentTest(unittest.TestCase):
    def set(self) -> None:
        self.__rep = Repository()
        self.__service = StudentService(self.__rep)

    def test_update(self):
        stud = Student('1232', "J", 100)
        self.__rep.add(stud)
        stud = Student('1234', "J", 101)
        self.__rep.add(stud)
        stud = Student('1233', "J", 100)
        self.__rep.add(stud)

        self.__service.update('1232', "E", None)
        self.__service.update('1234', None, 104)
        self.__service.update('1233', "K", 108)

        self.assertEqual(self.__rep["1232"].name, "E")
        self.assertEqual(self.__rep["1234"].group, 104)
        self.assertEqual(self.__rep["1233"].name, "K")
        self.assertEqual(self.__rep["1233"].group, 108)

    def test_add(self):
        self.__service.add("1234", "J", 100)
        self.assertEqual(len(self.__rep.database), 1)

    def test_remove(self):
        stud = Student("12341", "J", "A")
        self.__rep.add(stud)
        self.__service.remove("12341")
        self.assertEqual(len(self.__rep.database), 0)
