import unittest

from src.repository.repository import Repository
from src.services.assignment_services import AssignmentService
from src.services.grade_services import GradeService
from src.services.statistic_services import StatisticService
from src.services.student_services import StudentService
from src.services.undo_service import UndoService
from src.ui.ui import UI


def main():
    s_repo = Repository()
    a_repo = Repository()
    g_repo = Repository()
    a_service = AssignmentService(a_repo)
    s_service = StudentService(s_repo)
    g_service = GradeService(g_repo)
    u_service = UndoService(s_service, a_service, g_service)
    st_service = StatisticService(s_service, a_service, g_service)
    ui = UI(s_service, a_service, g_service, st_service, u_service)

    s_service.random_data()
    a_service.random_data()
    g_service.random_data(s_repo, a_repo)

    ui.start()
    unittest.main()


if __name__ == "__main__":
    main()
