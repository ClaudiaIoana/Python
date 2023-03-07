from datetime import date


class StatisticService:
    def __init__(self, student_service, assignment_service, grade_service):
        self.__student_service = student_service
        self.__assignment_service = assignment_service
        self.__grade_service = grade_service

    def list_order(self, assi):
        """The function creates a list of the students that have an assignment that is graded"""
        listi = []
        n = len(self.__grade_service.database)
        for ids in range(0, n):
            if assi == self.__grade_service.database[ids].assign_id and self.__grade_service.database[ids].grade \
                    is not None:
                val = (self.__grade_service.database[ids].student_id, self.__grade_service.database[ids].grade)
                listi.append(val)
        return listi

    def takeSecond(self, elem):
        return elem[1]

    def desc_order(self, assi):
        """The function puts the elements in descending order"""
        li = self.list_order(assi)
        li.sort(key=self.takeSecond, reverse=True)
        return li

    def unique(self, sid, l):
        """ The function searches if the student already has a given assignment. """
        n = len(l)
        for ids in range(0, n):
            if sid == l[ids]:
                return False
        return True

    def list_assi(self):
        """The function creates a list with all the students that are late in hanging at least one assignment. """
        li = []
        database = self.__assignment_service.database
        n = len(self.__grade_service.database)
        for i in range(0, n):
            if self.__grade_service.database[i].grade is None and self.unique(
                    self.__grade_service.database[i].student_id, li) is True:
                data = date.today()
                ids = self.__grade_service.database[i].assign_id
                if data > database[ids].deadline:
                    li.append(self.__grade_service.database[i].student_id)
        return li

    def med(self, sid):
        """the function calculates the average for a given student."""
        sum = 0
        nr = 0
        n = len(self.__grade_service.database)
        database = self.__grade_service.database
        for i in range(0, n):
            if self.__grade_service.database[i].student_id == sid:
                if database[i].grade is not None:
                    nr = nr + 1
                    sum = sum + database[i].grade
        if nr == 0:
            return 0
        else:
            return sum/nr

    def list_med(self):
        """The function creates a list with the average of every student."""
        l = []
        database = self.__student_service.database
        for ids in database:
            s = database[ids].id
            val = self.med(s)
            if val != 0:
                li = (s, val)
                l.append(li)
        return l

    def med_order(self):
        """The function puts the elements in a descending order"""
        list_of = self.list_med()
        list_of.sort(key=lambda l: l[1], reverse=True)
        return list_of
