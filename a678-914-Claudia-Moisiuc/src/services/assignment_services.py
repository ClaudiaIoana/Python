import random
from datetime import date

from src.domain.assignment import Assignment
from src.domain.validators import UniqueError


class AssignmentService:
    def __init__(self, repository):
        self.__repository = repository

    @property
    def database(self):
        """The function returns the assignments"""
        return self.__repository.database

    def unique(self, _id):
        """The program searches if a given id is unique"""
        assignments = self.__repository.database
        for ids in assignments:
            if _id == assignments[ids].id:
                return False
        return True

    def verify_unique(self, _id):
        """Raises an error if the given id already exists."""
        if self.unique(_id) is False:
            raise UniqueError("*This id already exists.*")

    def verify_existence(self, _id):
        """Raises an error if the given id doesn't exist."""
        if self.unique(_id) is True:
            raise UniqueError("*This id doesn't exist*")

    def random_data(self):
        """The function generates random data for the 20 start up assignments"""
        ai = ['write an essay on the topic: current situation', 'write an essay on the topic: music',
              'write an essay on the topic: jobs', 'write an essay on the topic: clothes',
              'write an essay on the topic: news', 'write an essay on the topic: sports',
              'write an essay on the topic: where you are living', 'write an essay on the topic: the future',
              'write an essay on the topic: how you spend your free time', 'write an essay on the topic: music',
              'write an essay on the topic: movies', 'write an essay on the topic: food',
              'write an essay on the topic: books', 'write an essay on the topic: TV',
              'write an essay on the topic: travel', 'write an essay on the topic: hobbies',
              'write an essay on the topic: children', 'write an essay on the topic: pets',
              'write an essay on the topic: restaurants', 'write an essay on the topic: movies',
              'write an essay on the topic: food', 'write an essay on the topic: books',
              'write an essay on the topic: movies', 'write an essay on the topic: food',
              'write an essay on the topic: books', 'write an essay on the topic: TV']
        for i in range(20):
            ok = False
            while not ok:
                id = int(random.randint(100, 999))
                ok = self.unique(id)
            deadline = date(random.randint(2012, 2024), random.randint(1, 12), random.randint(1, 27))
            a = Assignment(id, ai[random.randint(0, 21)], deadline)
            self.__repository.add(a)

    def add(self, id, desc, deadline):
        """The function adds an assignment if the assignment does not already exist."""
        if self.verify_unique(id) is False:
            raise UniqueError('*The id already exists*')
        else:
            new = Assignment(id, desc, deadline)
            self.__repository.add(new)

    def remove(self, id):
        """The function removes an assignment by is if it exists. """
        self.verify_existence(id)
        self.__repository.remove(id)

    def update(self, idd, desc=None, deadline=None):
        """The function updates the data for a given assignment. """
        self.verify_existence(idd)
        if desc and deadline is not None:
            new = Assignment(idd, desc, deadline)
        elif desc is None:
            des = self.__repository[idd].description
            new = Assignment(idd, des, deadline)
        else:
            deadlin = self.__repository[idd].deadline
            new = Assignment(idd, desc, deadlin)

        self.__repository.update(idd, new)