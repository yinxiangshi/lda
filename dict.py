'''
this file is a source code of double ways dict
'''


class Bidict(object):

    def __init__(self):
        '''
        create two dict
        dict:forward dict
        dict_rersed: reversed dict
        '''
        self.dict = {}
        self.dict_reversed = {}
        return

    def __len__(self):
        '''
        get the length of dict
        '''
        return len(self.dict)

    def __str__(self):
        '''
        turn dict type to string type
        '''
        str_list = ["%s\t%s" % (key, self.dict[key]) for key in self.dict]
        return "\n".join(str_list)

    def clear(self):
        '''
        clean dict
        :param self: dict
        '''
        self.dict.clear()
        self.dict_reversed.clear()
        return

    def add_key_value(self, key, value):
        '''
        update key~value
        '''
        self.dict[key] = value
        self.dict_reversed[value] = key
        return

    def remove_key_value(self, key, value):
        '''
        remove key~value
        '''
        if key in self.dict:
            del self.dict[key]
            del self.dict_reversed[value]
            return

    def get_value(self, key, default=None):
        '''
        get value through key,if haven't this key,return None
        '''
        return self.dict.get(key, default)

    def get_key(self, value, default=None):
        '''
        get key through value,if haven't this key,return None
        '''
        return self.dict_reversed.get(value, default)

    def contains_key(self, key):
        '''
        judge key in dict
        '''
        return key in self.dict

    def contins_value(self, value):
        '''
        judge value in dict
        '''
        return value in self.dict_reversed

    def get_all_keys(self):
        return self.dict.keys()

    def get_all_values(self):
        return self.dict_reversed.keys()

    def get_all(self):
        return self.dict.items()


if __name__ == '__main__':
    print('do not run in dict file')