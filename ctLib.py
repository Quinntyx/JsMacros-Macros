class StorageBlock:
    def __init__(self, position=None, input_dict=None):  # only leave position unset if planning to load from dict
        if input_dict is None:
            input_dict = {}
        if input_dict:
            self.position = input_dict['position']
            self.data = input_dict['data']
            return
        if position:
            self.position = (position.getX(), position.getY(), position.getZ())
        self.data = {}

    def add_item(self, slot, item, amount):
        self.data[slot] = (item, amount)

    def __str__(self):
        return str(" ".join(list(map(str, self.position))) + ": " + str(self.data))

    @staticmethod
    def keys():
        return ['position', 'data']

    def __getitem__(self, key):
        return getattr(self, key)

    def get_item(self, item):
        """Returns the number of items by the name item."""
        print(self.data)
        out = 0
        for i in self.data.keys():
            if self.data[i][0] == item:
                out += self.data[i][1]
        return out

    def has_item(self, item):
        """Returns True if the StorageBlock has the item, else False."""
        print(self.data)
        for i in self.data.keys():
            if self.data[i][0] == item:
                return True
        return False

    @property
    def name(self):
        return ' '.join(list(map(str, self.position)))


def name_to_id(name):
    if ':' in name:
        return name
    else:
        return f"minecraft:{name}"


def id_to_name(ID):
    if ':' in ID:
        return ID.split(':')[1]
    else:
        return ID


def make_safe(path):
    """Returns a version of the path that is safe for writing files to."""
    return ''.join([i if i not in [':', '.'] else '_' for i in path.split('/')[0]])
