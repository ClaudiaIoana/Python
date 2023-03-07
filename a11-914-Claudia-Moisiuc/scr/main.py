import pygame
from configparser import ConfigParser
from scr.gui.gui import GUI
from scr.repository.repository import Repository
from scr.service.service import Service
from scr.ui.ui import UI


def main():
    parser = ConfigParser()
    parser.read("settings.properties")
    settings = parser.get("options", "ui")

    repository = Repository()
    service = Service(repository)

    if settings == "ui":
        ui = UI(service, repository)
        ui.valid_game()
    elif settings == "gui":
        gui = GUI(repository, service)
        gui.make_board()

if __name__ == "__main__":
    main()