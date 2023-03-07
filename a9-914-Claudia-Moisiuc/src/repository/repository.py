import os
import pickle

from src.domain.student import Student



class Repository(object):
    def __init__(self):
        self.__entity_dict = dict()
        self.__entity_list = list()

    def set(self, dict):
        self.__entity_dict = dict

    def setl(self, list):
        self.__entity_list = list

    @property
    def database(self):
        return self.__entity_dict

    def __getitem__(self, _id):
        return self.__entity_dict[_id]

    def entity_with_id(self, _id):
        return self.__entity_dict[_id]

    @property
    def databaseg(self):
        return self.__entity_list

    def add(self, entity):
        self.__entity_dict[entity.id] = entity

    def add_g(self, entity):
        self.__entity_list.append(entity)

    def remove_g(self, i):
        del self.__entity_list[i]

    def update_g(self, i, new_entity):
        self.__entity_list[i] = new_entity

    def remove(self, _id):
        del self.__entity_dict[_id]

    def update(self, _id, new_entity):
        self.__entity_dict[_id] = new_entity

class STextFileRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            id, name, group = line.split(',')
            super().add(Student(int(id), name, int(group)))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')
        for student in self.database.values():
            f.write(str(student.id)+','+student.name+','+str(student.group)+'\n')
        f.close()

    def add(self, entity):
        super(STextFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(STextFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove(self, entity_id):
        super(STextFileRepository, self).remove(entity_id)
        self._save_file()

class ATextFileRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load_file()

    def _load_file(self):
        f = open(self._file_name, 'rt')
        for line in f.readlines():
            #print(line)
            id, des, de = line.split(',')
            d = de.removesuffix("\n")
            from src.domain.assignment import Assignment
            super().add(Assignment(int(id), des, d))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')
        for assignment in self.database.values():
            f.write(str(assignment.id)+','+assignment.description+','+str(assignment.deadline))
        f.close()

    def add(self, entity):
        super(ATextFileRepository, self).add(entity)
        self._save_file()

    def update(self, entity_id, entity):
        super(ATextFileRepository, self).update(entity_id, entity)
        self._save_file()

    def remove(self, entity_id):
        super(ATextFileRepository, self).remove(entity_id)
        self._save_file()

class GTextFileRepository(Repository):
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
                super().add_g(Grade(int(ida), int(ids), g))
            else:
                super().add_g(Grade(int(ida), int(ids), g))

        f.close()

    def _save_file(self):
        f = open(self._file_name, 'wt')
        n = len(self.databaseg)
        for grade in range(0, n):
            f.write(str(self.databaseg[grade].assign_id)+','+str(self.databaseg[grade].student_id)+','+str(self.databaseg[grade].grade)+'\n')
        f.close()

    def add_g(self, entity):
        super(GTextFileRepository, self).add_g(entity)
        self._save_file()

    def remove_g(self, entity_id):
        super(GTextFileRepository, self).remove_g(entity_id)
        self._save_file()

    def update_g(self, i, entity_id):
        super(GTextFileRepository, self).update_g(i, entity_id)
        self._save_file()

class SBinaryFileRepository(Repository):
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

    def add(self, entity):
        super(SBinaryFileRepository, self).add(entity)
        self.save_file()

    def update(self, entity_id, entity):
        super(SBinaryFileRepository, self).update(entity_id, entity)
        self.save_file()

    def remove(self, entity_id):
        super(SBinaryFileRepository, self).remove(entity_id)
        self.save_file()

class ABinaryFileRepository(Repository):
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

    def add(self, entity):
        super(ABinaryFileRepository, self).add(entity)
        self.save_file()

    def update(self, entity_id, entity):
        super(ABinaryFileRepository, self).update(entity_id, entity)
        self.save_file()

    def remove(self, entity_id):
        super(ABinaryFileRepository, self).remove(entity_id)
        self.save_file()

class GBinaryFileRepository(Repository):
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
        self.setl(p)
        f.close()

    def save_file(self):
        f = open(self.file_name, 'wb')
        pickle.dump(self.databaseg, f)
        f.close()

    def add_g(self, entity):
        super(GBinaryFileRepository, self).add_g(entity)
        self.save_file()

    def remove_g(self, entity_id):
        super(GBinaryFileRepository, self).remove_g(entity_id)
        self.save_file()

    def update_g(self, i, entity_id):
        super(GBinaryFileRepository, self).update_g(i, entity_id)
        self.save_file()
