
class UniqueKeyCollection(object):
    """Dict-like collection guaranteeing a unique integer key per value
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self._backing_dict = {}

    def _get_next_key(self):
        key = 0
        while key in self._backing_dict:
            key += 1
        return key

    def insert(self, val):
        """Add val to the collection and return the new key
        """
        key = self._get_next_key()
        assert key not in self._backing_dict

        self._backing_dict[key] = val
        return key

    def remove(self, key):
        """Remove the value associated with the key
        """
        del self._backing_dict[key]

    def get(self, key):
        """Return the value associated with key or raise KeyError
        """
        return self._backing_dict[key]

    def __contains__(self, key):
        return key in self._backing_dict

