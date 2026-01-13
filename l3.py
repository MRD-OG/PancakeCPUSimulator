from cache import Cache
from enum import Enum


class Meta_ENUM(Enum):
    VALID     = 0
    DIRTY     = 1
    REF_COUNT = 2


class L3(Cache):

    def __init__(self, tag_mask, tag_offset, index_mask, index_offset, associativity, sets, line_size):
        super().__init__(tag_mask, tag_offset, index_mask, index_offset,  associativity, sets, line_size)

        self.tags = [[0 for _ in range(associativity)] for _ in range(sets)]
        # L3 metadata contains [valid bit, dirty bit, reference count]
        self.meta = [[[0, 0, 0] for _ in range(associativity)] for _ in range(sets)]

        self.buffer = None

    def set_shared_buffer(self, buffer):
        self.buffer = buffer

    def fetch(self, address, modify):
        (tag, index)    = self.get_tag_index(address)
        (hit, line_idx) = self.check_tag(tag, index)

        if hit:
            # convert valid, dirty, ref count to MESI
            # 00 - Invalid
            # 01 - Shared
            # 10 - Exclusive
            # 11 - Modified

            line_meta = self.meta[index][line_idx]
            v         = line_meta[Meta_ENUM.VALID.value]
            d         = line_meta[Meta_ENUM.DIRTY.value]
            rc        = line_meta[Meta_ENUM.REF_COUNT.value]
            data      = self.data[index][line_idx]
            meta      = 0b00

            # Modified
            if ((v == 1) and (d == 1) and rc == 0) or modify:
                meta  = 0b11
                # todo: queue invalidate to shared bus

            # Exclusive
            elif (v == 1) and (d == 0) and rc == 0:
                meta = 0b10
            # Shared
            elif (v == 1) and (d == 0) and rc > 0:
                meta  = 0b01

            return hit, data, meta

        else:
            # todo: fetch from main memory
            # todo: set metadata
            pass


    def flush(self, address):
        pass

    def write_back(self, address):
        pass

    def check_tag(self, tag, index):

        cache_set = self.tags[index]

        for (line_idx, stored_tag) in enumerate(cache_set):
            if stored_tag == tag:
                return True, line_idx

        return False, -1
