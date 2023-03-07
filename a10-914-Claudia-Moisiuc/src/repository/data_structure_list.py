
class RepositoryList(object):
    def __init__(self):
        self.entities = []

    def __iter__(self):
        self.poz = 0
        return self

    def __add__(self, val):
        self.entities.append(val)

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
        self.entities = list

    @property
    def database(self):
        return self.entities

    def sort(self):
        """We use shell sort to sort the data."""
        def comp_mare(a, b):
            if a > b:
                return True
            return False

        n = len(self.entities)
        gap = n // 2
        while gap > 0:
            i = gap
            while i < n:
                temp = self.entities[i]
                j = i
                while comp_mare(j, gap-1) is True and comp_mare(self.entities[j - gap].assign_id, temp.assign_id)\
                        is True:
                    self.entities[j] = self.entities[j - gap]
                    j = j - gap
                self.entities[j] = temp
                i = i + 1
            gap = gap // 2
        return self.entities

    def filter_note(self):
        def valid_note(a):
            if a < 5:
                return False
            return True
        n = len(self.entities)
        i = 0
        while i < n:
            if self.entities[i].grade is not None:
                if valid_note(self.entities[i].grade) is False:
                    self.__delitem__(i)
                    n = n - 1
                else:
                    i = i + 1
        return self.entities