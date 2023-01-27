#!/usr/bin/python3
''' MRU Caching '''

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' MRU Caching '''

    def __init__(self):
        super().__init__()
        self.mru_keys_order = OrderedDict()

    def put(self, key, item):
        ''' insert item to dict '''
        if not key or not item:
            return

        self.cache_data[key] = item
        self.mru_keys_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_keys_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_keys_order) > BaseCaching.MAX_ITEMS:
            self.mru_keys_order.popitem(last=False)

        self.mru_keys_order.move_to_end(key, False)

    def get(self, key):
        ''' get item from dict '''
        if key in self.cache_data:
            self.mru_keys_order.move_to_end(key, False)
            return self.cache_data[key]
        return None
