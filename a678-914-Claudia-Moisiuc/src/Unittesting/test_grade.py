import unittest

from src.domain.grade import Grade
from src.repository.repository import Repository
from src.services.grade_services import GradeService


class GradeTest(unittest.TestCase):

    def set(self) -> None:
        self.__repo = Repository()
        self.__service = GradeService(self.__repo)

    def test_give_grade(self):
        assi = Grade(1232, 51, None)
        self.__repo.add(assi)
        self.__service.give_grade(1232, 51, 7)
        self.assertEqual(self.__repo["1232"].grade, 7)

    def test_add(self):
        self.__service.add(1234, 12, 7)
        self.assertEqual(len(self.__repo.database), 1)

    def test_remove(self):
        assi = Grade(12341, 45, 3)
        self.__repo.add(assi)
        self.__service.remove(12341)
        self.assertEqual(len(self.__repo.database), 0)

        assi = Grade(12341, 45, 3)
        self.__repo.add(assi)
        self.__service.removes(45)
        self.assertEqual(len(self.__repo.database), 0)
