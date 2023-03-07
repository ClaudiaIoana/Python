import random

from src.domain.grade import Grade
from src.domain.validators import UniqueError



class GradeService:
    def __init__(self, repository):
        self.__repository = repository

    @property
    def database(self):
        return self.__repository.databaseg

    def random_data(self, student_repository, assignment_repository):
        '''The function generates 20 start up random data. '''
        stud = student_repository.database
        assi = assignment_repository.database

        for i in range(20):
            id_stud = random.choice(list(stud))
            id_assi = random.choice(list(assi))
            while self.availability(id_stud) is False:
                id_stud = random.choice(list(stud))
            while self.availability(id_assi) is False:
                id_assi = random.choice(list(assi))
            new = Grade(id_assi, id_stud, random.randint(1,10))
            self.__repository.add_g(new)

    def availability(self, id):
        '''The function verifies if an id is available. '''
        n = len(self.__repository.databaseg)
        for ids in range (0, n):
            if id == self.__repository.databaseg[ids]:
                return False
        return True

    def existence(self, sid):
        '''The function verifies if a student has any assignments. '''
        n = len(self.__repository.databaseg)
        for ids in range(0, n):
            if sid == self.__repository.databaseg[ids].student_id:
                return True
        return False

    def verify_existence(self, i):
        '''Raises an error if the given id doesn't exist. '''
        if self.existence(i) is False:
            raise UniqueError("*This id doesn't exist*")

    def graded(self, sid, aid):
        '''The function verifies if the assignment already has been graded. '''
        n = len(self.__repository.databaseg)
        for ids in range(0, n):
            if sid == self.__repository.databaseg[ids].student_id and aid == self.__repository.databaseg[ids].assign_id:
                if self.__repository.databaseg[ids].grade is not None:
                    raise UniqueError('The assignment already has a grade. ')

    def give_grade(self, sid, aid, gr=None):
        '''The function grades the assignments. '''
        if gr != None:
            self.graded(sid, aid)
        n = len(self.__repository.databaseg)
        for i in range(0, n):
            if sid == self.__repository.databaseg[i].student_id and aid == self.__repository.databaseg[i].assign_id:
                g = Grade(aid, sid, gr)
                self.__repository.update(i, g)

    def unique(self, sid, aid):
        ''' The function searches if the student already has a given assignment. '''
        n = len(self.__repository.databaseg)
        for ids in range(0, n):
            if sid == self.__repository.databaseg[ids].student_id and aid == self.__repository.databaseg[ids].assign_id:
                return False
        return True

    def verify_unique(self, sid, aid):
        '''Raises an error if the given ids doesn't exist. '''
        if self.unique(sid, aid) is True:
            raise UniqueError("*Those ids don't exist*")

    def add(self,aid, sid, grade=None):
        '''The function adds a student and an assignment. '''
        if self.unique(sid, aid) is not False:
            gr = Grade(aid, sid, grade)
            self.__repository.add_g(gr)

    def remove(self, id):
        '''The function removes an assignment by is if it exists. '''
        n = len(self.__repository.databaseg)
        ids = 0
        while ids < n:
            if id == self.__repository.databaseg[ids].assign_id:
                self.__repository.remove_g(ids)
                n = n - 1
            else:
                ids = ids + 1

    def removes(self, id):
        '''The function removes an student by is if it exists. '''
        n = len(self.__repository.databaseg)
        ids = 0
        while ids < n:
            if id == self.__repository.databaseg[ids].student_id:
                self.__repository.remove_g(ids)
                n = n - 1
            else:
                ids = ids + 1

    def remov(self, l, ida):
        n = len(l)
        for i in range (0, n):
            self.remo(l[i], ida)

    def ad(self, l, ida):
        n = len(l)
        for i in range(0, n):
            self.add_g(ida, l[i])

    def remo(self, ids, ida):
        n = len(self.__repository.databaseg)
        idd = 0
        while idd < n:
            if ids == self.__repository.databaseg[idd].student_id and ida == self.__repository.databaseg[idd].assign_id:
                self.__repository.remove_g(idd)
                n = n - 1
            else:
                idd = idd + 1