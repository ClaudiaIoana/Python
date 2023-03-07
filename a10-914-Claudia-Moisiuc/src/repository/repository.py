import os
import pickle

from src.domain.student import Student
from src.repository.data_structure_dict import RepositoryDict
from src.repository.data_structure_list import RepositoryList


class STextFileRepository(RepositoryDict):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            id, name, group = line.split(',')
            super().__add__(Student(int(id), name, int(group)))
        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')
        for student in self.database.values():
            f.write(str(student.id)+','+student.name+','+str(student.group)+'\n')
        super(STextFileRepository, self).sort()
        f.close()

    def __add__(self, entity):
        super(STextFileRepository, self).__add__(entity)
        super(STextFileRepository, self).sort()
        self._save_file()

    def __setitem__(self, entity_id, entity):
        super(STextFileRepository, self).__setitem__(entity_id, entity)
        self._save_file()

    def __delitem__(self, entity_id):
        super(STextFileRepository, self).__delitem__(entity_id)
        self._save_file()


class ATextFileRepository(RepositoryDict):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            # print(line)
            id, des, de = line.split(',')
            d = de.removesuffix("\n")
            from src.domain.assignment import Assignment
            super().__add__(Assignment(int(id), des, d))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')
        for assignment in self.database.values():
            f.write(str(assignment.id)+','+assignment.description+','+str(assignment.deadline)+'\n')
        f.close()

    def __add__(self, entity):
        super(ATextFileRepository, self).__add__(entity)
        self._save_file()

    def __setitem__(self, entity_id, entity):
        super(ATextFileRepository, self).__setitem__(entity_id, entity)
        self._save_file()

    def __delitem__(self, entity_id):
        super(ATextFileRepository, self).__delitem__(entity_id)
        self._save_file()


class GTextFileRepository(RepositoryList):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            ida, ids, gr = line.split(',')
            g = gr.removesuffix("\n")
            print(g)
            from src.domain.grade import Grade
            if g is None:
                super().__add__(Grade(int(ida), int(ids), g))
            else:
                super().__add__(Grade(int(ida), int(ids), g))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')
        n = len(self.database)
        for grade in range(0, n):
            f.write(str(self.database[grade].assign_id)+','+str(self.database[grade].student_id)+','
                    +str(self.database[grade].grade)+'\n')
        f.close()

    def __add__(self, entity):
        super(GTextFileRepository, self).__add__(entity)
        self._save_file()

    def __delitem__(self, entity_id):
        super(GTextFileRepository, self).__delitem__(entity_id)
        self._save_file()

    def __setitem__(self, i, entity_id):
        super(GTextFileRepository, self).__setitem__(i, entity_id)
        self._save_file()


class SBinaryFileRepository(RepositoryDict):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        filesize = os.path.getsize(self.file_name)
        if filesize == 0:
            pass
        else:
            self.load_file()

    def load_file(self):
        f = open(self.file_name, "rb")
        p = pickle.load(f)
        self.set(p)
        f.close()

    def save_file(self):
        f = open(self.file_name, 'wb')
        pickle.dump(self.database, f)
        f.close()

    def __add__(self, entity):
        super(SBinaryFileRepository, self).__add__(entity)
        self.save_file()

    def __delitem__(self, entity_id, entity):
        super(SBinaryFileRepository, self).__setitem__(entity_id, entity)
        self.save_file()

    def __setitem__(self, entity_id):
        super(SBinaryFileRepository, self).__delitem__(entity_id)
        self.save_file()


class ABinaryFileRepository(RepositoryDict):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        filesize = os.path.getsize(self.file_name)
        if filesize == 0:
            pass
        else:
            self.load_file()

    def load_file(self):
        f = open(self.file_name, 'rb')
        p = pickle.load(f)
        self.set(p)
        f.close()

    def save_file(self):
        f = open(self.file_name, 'wb')
        pickle.dump(self.database, f)
        f.close()

    def __add__(self, entity):
        super(ABinaryFileRepository, self).__add__(entity)
        self.save_file()

    def __delitem__(self, entity_id, entity):
        super(ABinaryFileRepository, self).__setitem__(entity_id, entity)
        self.save_file()

    def __setitem__(self, entity_id):
        super(ABinaryFileRepository, self).__delitem__(entity_id)
        self.save_file()


class GBinaryFileRepository(RepositoryList):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        filesize = os.path.getsize(self.file_name)
        if filesize == 0:
            pass
        else:
            self.load_file()

    def load_file(self):
        f = open(self.file_name, 'rb')
        p = pickle.load(f)
        self.set(p)
        f.close()

    def save_file(self):
        f = open(self.file_name, 'wb')
        pickle.dump(self.database, f)
        f.close()

    def __add__(self, entity):
        super(GBinaryFileRepository, self).__add__(entity)
        self.save_file()

    def __delitem__(self, entity_id):
        super(GBinaryFileRepository, self).__delitem__(entity_id)
        self.save_file()

    def __setitem__(self, i, entity_id):
        super(GBinaryFileRepository, self).__setitem__(i, entity_id)
        self.save_file()
