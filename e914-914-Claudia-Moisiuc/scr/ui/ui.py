
class UI:
    def __init__(self, repository, service):
        self.__repository = repository
        self.__service = service

    def play(self):
        self.__service.asteroids()
        self.__service.alien()
        self.print_board()
        ok=0
        while ok != 2:
            inputing = input("COORDINATES FOR FIRE:   ")
            if inputing == "cheat":
                self.print_cheat()
            else:
                val = ord(inputing[0])-ord('A')
                while self.__service.fire_valid(int(inputing[1])-1, int(val+1)) == False:
                    print("Invalid input. Try again")
                    inputing = input("COORDINATES FOR FIRE:   ")
                    val = ord(inputing[0]) - ord('A')
                if self.__service.fire(int(inputing[1])-1, int(val+1)) == 'hit':
                    print('Hit. Alien ship destroyed.')
                    self.print_board()
                    ok=ok+1

        if ok == 2:
            print("YOU WON!  ")

    def print_board(self):
        print(self.__repository.get_texttable().draw())

    def print_cheat(self):
        print(self.__repository.get_cheat().draw())

#