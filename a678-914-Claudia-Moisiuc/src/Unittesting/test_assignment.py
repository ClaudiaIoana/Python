import unittest

from src.domain.assignment import Assignment
from src.repository.repository import Repository
from src.services.assignment_services import AssignmentService


class AssignmentTest(unittest.TestCase):

    def set(self) -> None:
        self.__repo = Repository()
        self.__service = AssignmentService(self.__repo)

    def test_update(self):

        assi = Assignment('1232', "J", 2020-2-23)
        self.__repo.add(assi)
        assi = Assignment("1234", "J", 2020-2-23)
        self.__repo.add(assi)
        assi = Assignment("1233", "J", 2020-2-23)
        self.__repo.add(assi)

        self.__service.update("1232", "E", None)
        self.__service.update("1234", None, 2020-12-23)
        self.__service.update("1233", "K", 2020-11-23)

        self.assertEqual(self.__repo["1232"].description, "E")
        self.assertEqual(self.__repo["1234"].deadline, 2020-12-23)
        self.assertEqual(self.__repo["1233"].description, "K")
        self.assertEqual(self.__repo["1233"].deadline, 2020-11-23)

    def test_add(self):
        self.__service.add("1234", "J", 2020-12-23)
        self.assertEqual(len(self.__repo.database), 1)

    def test_remove(self):
        assi = Assignment("12341", "J", 2020-12-23)
        self.__repo.add(assi)
        self.__service.remove("12341")
        self.assertEqual(len(self.__repo.database), 0)

