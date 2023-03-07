import random
import names

from src.services.services import Service, test


def id_in(stud, idi):
    '''
    the function tests if the id is unique
    :param stud: the list
    :param idi: the id
    :return: 0 if it is not unique and 1 if it is unique
    '''
    n = len(stud)
    for i in range(0, n):
        # print(stud[i].id, idi)
        if stud[i]._id == idi:
            return 0
    return 1


class Student:
    """
    We define a class to memorize the data of the students
    """
    def __init__(self, id, name, group):
        self._id = id
        self.name = name
        self.group = group

    def rand_id(self, stud):
        idd = int(random.randint(10000, 99999))
        ok = True
        while ok:
            if id_in(stud, idd) == 0:
                idd = int(random.randint(10000, 99999))
            else:
                ok = False
        return idd

    def rand_nm(self):
        return names.get_full_name()

    def rand_gr(self):
        return random.randint(100,107)


if __name__ == '__main__':
    f = Service()
    stud = []
    test(f)
    from src.ui.ui import Out
    outi = Out()
    outi.print_menu()
    elim = []
    f.auto_set(stud)
    f.menu(stud, elim, outi, f)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
