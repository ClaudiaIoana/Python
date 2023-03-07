import datetime
import unittest

from src.domain.assignment import Assignment
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.data_structure_dict import RepositoryDict
from src.repository.data_structure_list import RepositoryList
from src.services.assugnment_services import AssignmentService
from src.services.grade_services import GradeService
from src.services.student_services import StudentService
from src.services.undo_redo_services import UndoService



class AssignmentTest(unittest.TestCase):

    def setUp(self) -> None:
        self.repository = RepositoryDict()
        self.service = AssignmentService(self.repository)

    def test_update(self):

        assi = Assignment('1232', "J", 2020-2-23)
        self.repository.__add__(assi)
        assi = Assignment("1234", "J", 2020-2-23)
        self.repository.__add__(assi)
        assi = Assignment("1233", "J", 2020-2-23)
        self.repository.__add__(assi)

        self.service.update("1232", "E", None)
        self.service.update("1234", None, 2020-12-23)
        self.service.update("1233", "K", 2020-11-23)

        self.assertEqual(self.repository["1232"].description, "E")
        self.assertEqual(self.repository["1234"].deadline, 2020-12-23)
        self.assertEqual(self.repository["1233"].description, "K")
        self.assertEqual(self.repository["1233"].deadline, 2020-11-23)

    def test_add(self):

        self.service.add("1234", "J", 2020-12-23)
        self.assertEqual(len(self.repository.database), 1)

    def test_remove(self):

        assi = Assignment("12341", "J", 2020-12-23)
        self.repository.__add__(assi)
        self.service.remove("12341")
        self.assertEqual(len(self.repository.database), 0)

    def test_unique(self):

        assi = Assignment(12341, "J", 2020 - 12 - 23)
        self.repository.__add__(assi)
        self.assertEqual(self.service.unique(12341), False)
        self.assertEqual(self.service.unique(1231), True)

    def test_find_by_id(self):

        assi = Assignment(1232, "J", 2020 - 2 - 23)
        self.repository.__add__(assi)
        assi = Assignment(1234, "J", 2020 - 2 - 23)
        self.repository.__add__(assi)
        assi = Assignment(1233, "J", 2020 - 2 - 23)
        self.repository.__add__(assi)

        self.assertEqual(self.service.find_by_id(124), None)


class GradeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.repository = RepositoryList()
        self.service = GradeService(self.repository)

    def test_give_grade(self):
        assi = Grade(1232, 51, 7)
        self.repository.__add__(assi)
        self.service.give_grade(1232, 51, 9)
        self.assertEqual(self.repository[0].grade, 7)

    def test_add(self):
        self.service.add(1234, 12, 7)
        self.assertEqual(len(self.repository.database), 1)

    def test_remove(self):
        assi = Grade(12341, 45, 3)
        self.repository.__add__(assi)
        self.service.remove(12341)
        self.assertEqual(len(self.repository.database), 0)

        assi = Grade(12341, 45, 3)
        self.repository.__add__(assi)
        self.service.removes(45)
        self.assertEqual(len(self.repository.database), 0)

    def test_unique(self):
        assi = Grade(1231, 43, 3)
        self.repository.__add__(assi)
        assi = Grade(12341, 45, 3)
        self.repository.__add__(assi)
        self.assertEqual(self.service.unique(12341, 43), True)

    def test_sort(self):
        assi = Grade(1231, 43, 3)
        self.repository.__add__(assi)
        assi = Grade(121, 45, 3)
        self.repository.__add__(assi)
        self.service.sort()
        self.assertEqual(self.repository.database[0].assign_id, 121)


class StudentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = RepositoryDict()
        self.service = StudentService(self.repository)

    def test_update(self):
        stud = Student('1232', "J", 100)
        self.repository.__add__(stud)
        stud = Student('1234', "J", 101)
        self.repository.__add__(stud)
        stud = Student('1233', "J", 100)
        self.repository.__add__(stud)

        self.service.update('1232', "E", None)
        self.service.update('1234', None, 104)
        self.service.update('1233', "K", 108)

        self.assertEqual(self.repository["1232"].name, "E")
        self.assertEqual(self.repository["1234"].group, 104)
        self.assertEqual(self.repository["1233"].name, "K")
        self.assertEqual(self.repository["1233"].group, 108)

    def test_add(self):
        self.service.add("1234", "J", 100)
        self.assertEqual(len(self.repository.database), 1)

    def test_remove(self):
        stud = Student("12341", "J", "A")
        self.repository.__add__(stud)
        self.service.remove("12341")
        self.assertEqual(len(self.repository.database), 0)

    def test_unique(self):

        assi = Student(12341, "J", 100)
        self.repository.__add__(assi)
        self.assertEqual(self.service.unique(1231), True)

    def test_find_by_id(self):

        assi = Student(1232, "J", 100)
        self.repository.__add__(assi)
        assi = Student(1234, "J", 100)
        self.repository.__add__(assi)
        assi = Student(1233, "J", 100)
        self.repository.__add__(assi)

        self.assertEqual(self.service.find_by_id(124), None)


class DomainTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = RepositoryDict()
        self.service = StudentService(self.repository)

    def test_assignment(self):
        asi = Assignment(182, "lasjdd", 2020 - 2 - 4)
        self.assertEqual(asi.id, 182)
        self.assertEqual(asi.description, "lasjdd")
        self.assertEqual(asi.deadline, 2020 - 2 - 4)

    def test_student(self):
        asi = Student(182, "lasjdd", 2020)
        self.assertEqual(asi.id, 182)
        self.assertEqual(asi.name, "lasjdd")
        self.assertEqual(asi.group, 2020)

    def test_grade(self):
        asi = Grade(182, 32, 4)
        self.assertEqual(asi.student_id, 32)
        self.assertEqual(asi.assign_id, 182)
        self.assertEqual(asi.grade, 4)

    def test_sort(self):
        assi = Student(1232, "Ji", 100)
        self.repository.__add__(assi)
        assi = Student(1234, "Jo", 100)
        self.repository.__add__(assi)
        assi = Student(1233, "Ju", 100)
        self.repository.__add__(assi)

        self.repository.sort()
        self.assertEqual(self.repository.database[1232].name,'Ji')
        self.assertEqual(self.repository.database[1233].name, 'Ju')
        self.assertEqual(self.repository.database[1234].name,'Jo')

    def test_filter(self):
        assi = Assignment(1232, "J", 2020 - 2 - 23)
        self.repository.__add__(assi)
        assi = Assignment(1234, "J", 2021 - 2 - 23)
        self.repository.__add__(assi)
        assi = Assignment(1233, "J", 2020 - 2 - 23)
        self.repository.__add__(assi)
        self.assertEqual(len(self.repository.database), 3)
