import unittest

from src.repository.repository import Repository
from src.services.assignment_services import AssignmentService
from src.services.grade_services import GradeService
from src.services.student_services import StudentService
from src.services.undo_service import UndoService


class UndoTest(unittest.TestCase):

    def set(self) -> None:
        self._repo = Repository()
        self._a_service = AssignmentService(self._repo)
        self._s_service = StudentService(self._repo)
        self._g_service = GradeService(self._repo)
        self._service = UndoService(self._s_service, self._a_service, self._g_service)
        self._undo_stack = []
        self._undo_pointer = 0

    def test_register_operation(self):
        self._a_service.add(123, 'd', 2020-3-4)
        operation = self._s_service.remove(123)
        self._service.register_operation(operation)
        self.assertEqual(len(self._undo_stack), 1)

    def test_undo(self):
        self._a_service.add(123, 'd', 2020 - 3 - 4)
        operation = self._s_service.remove(123)
        self._service.register_operation(operation)
        self._service.undo()
        self.assertEqual(len(self._undo_stack), 0)
        self._service.redo()
        self.assertEqual(len(self._undo_stack), 1)

