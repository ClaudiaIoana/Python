import unittest

from src.repository.repository import Repository
from src.services.assignment_services import AssignmentService
from src.services.grade_services import GradeService
from src.services.statistic_services import StatisticService
from src.services.student_services import StudentService


class StatisticTest(unittest.TestCase):

    def set(self) -> None:
        self.__repo = Repository()
        self.__a_service = AssignmentService(self.__repo)
        self.__s_service = StudentService(self.__repo)
        self.__g_service = GradeService(self.__repo)
        self.__st_service = StatisticService(self.__s_service, self.__a_service, self.__g_service)

    def test_list_order(self):
        self.__s_service.add(1234, 12, 7)
        self.assertEqual(len(self.__repo.database), 1)

    def test_med(self):
        self.__g_service.add(1234, 12, 7)
        self.__g_service.add(1234, 12, 9)
        self.assertEqual(self.__st_service.med(12), 8)

    def test_list_assi(self):
        self.__a_service.add(123, 'df', 2020-3-4)
        self.assertEqual(len(self.__st_service.list_assi()), 1)

