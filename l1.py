from cache import Cache


class L1(Cache):

    def __init__(self, tag_mask, tag_offset, index_mask, index_offset, associativity, sets, line_size):
        super().__init__(tag_mask, tag_offset, index_mask, index_offset,  associativity, sets, line_size)

    def fetch(self, address):
        pass

    def flush(self, address):
        pass

    def write_back(self, address):
        pass


