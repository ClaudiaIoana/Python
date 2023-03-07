from scr.repository.repository import Repository
from scr.service.service import Service
from scr.ui.ui import UI

def main():
    repo = Repository()
    serv = Service(repo)
    ui = UI(repo, serv)

    ui.play()

if __name__ == "__main__":
    main()
#