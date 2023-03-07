

class Repository(object):
    def __init__(self):
        self.__entity_dict = dict()
        self.__entity_list = list()

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

    def add_g(self, entity, i):
        self.__entity_list.append(entity)

    def remove_g(self, i):
        del self.__entity_list[i]

    def update_g(self, i, new_entity):
        self.__entity_list[i] = new_entity

    def remove(self, _id):
        del self.__entity_dict[_id]

    def update(self, _id, new_entity):
        self.__entity_dict[_id] = new_entity
