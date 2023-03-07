from datetime import date

from src.domain.assignment import Assignment
from src.domain.student import Student


class RepositoryDict(object):
    def __init__(self):
        self.entities = dict()

    def __iter__(self):
        self.poz = 0
        return self

    def __add__(self, val):
        self.entities[val.id] = val

    def __next__(self):
        if self.poz < len(self.entities):
            self.poz = self.poz + 1
            return self.entities[self.poz - 1]

    def __delitem__(self, key):
        del self.entities[key]

    def __setitem__(self, key, val):
        self.entities[key] = val

    def __getitem__(self, key):
        return self.entities[key]

    def set(self, list):
        self.entities = dict

    @property
    def database(self):
        return self.entities

    def sort_student(self):
        listi = self.sort()
        self.entities.clear()
        for i in range(0, len(listi)):
            s = Student(listi[i].id, listi[i].name, listi[i].group)
            self.__setitem__(listi[i].id, s)
        return self.entities

    def sort_assignment(self):
        listi = self.sort()
        self.entities.clear()
        for i in range(0, len(listi)):
            s = Assignment(listi[i].id, listi[i].description, listi[i].deadline)
            self.__setitem__(listi[i].id, s)
        return self.entities

    def sort(self):
        """We use shell sort to sort the data."""
        """We use shell sort to sort the data."""
        listi = list(self.entities.values())

        def comp_mare(a, b):
            if a > b:
                return True
            return False

        n = len(listi)
        gap = n // 2
        while gap > 0:
            i = gap
            while i < n:
                temp = listi[i]
                j = i
                while comp_mare(j, gap - 1) is True and comp_mare(listi[j - gap].id,
                                                                  temp.id) is True:
                    listi[j] = listi[j - gap]
                    j = j - gap
                listi[j] = temp
                i = i + 1
            gap = gap // 2

        return listi

    def filter_deadline(self):
        def valid_date(a):
            data = date.today()
            print(type(data))
            if data > a:
                return False
            return True
        keys_list = list(self.entities.keys())
        n = len(self.entities)
        i = 0
        while i < n:
            if valid_date(self.entities[keys_list[i]].deadline) is False:
                self.__delitem__(keys_list[i])
                n = n - 1
                del keys_list[i]
            else:
                i = i + 1
        return self.entities
