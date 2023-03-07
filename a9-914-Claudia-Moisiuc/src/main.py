import unittest

from configparser import ConfigParser

from src import settings
from src.repository.repository import Repository, STextFileRepository, ATextFileRepository, GTextFileRepository, \
    SBinaryFileRepository, ABinaryFileRepository, GBinaryFileRepository
from src.services.assugnment_services import AssignmentService
from src.services.grade_services import GradeService
from src.services.statistic_services import StatisticService
from src.services.student_services import StudentService
from src.services.undo_redo_services import UndoService
from src.settings import Settings
from src.ui.ui import UI


def main():

    parser = ConfigParser()
    parser.read("files/settings.properties")
    settings_dict = parser.get("options", "repository")

    if settings_dict == "inmemory":
        s_repos = Repository()
        a_repos = Repository()
        g_repos = Repository()
    elif settings_dict == "text":
        s_repos = STextFileRepository(parser.get("options", "student" ))
        a_repos = ATextFileRepository(parser.get("options", "assignment"))
        g_repos = GTextFileRepository(parser.get("options", "grade"))
    elif settings_dict == "pickle":
        s_repos = SBinaryFileRepository(parser.get("options", "student"))
        a_repos = ABinaryFileRepository(parser.get("options", "assignment"))
        g_repos = GBinaryFileRepository(parser.get("options", "grade"))

    a_service = AssignmentService(a_repos)
    s_service = StudentService(s_repos)
    g_service = GradeService(g_repos)
    u_service = UndoService(s_service, a_service, g_service)
    st_service = StatisticService(s_service, a_service, g_service)
    ui = UI(s_service, a_service, g_service, st_service, u_service)
    if settings_dict == "inmemory":
        s_service.random_data()
        a_service.random_data()
        g_service.random_data(s_repo, a_repo)
    ui.start()
    unittest.main()

if __name__ == "__main__":
    main()

