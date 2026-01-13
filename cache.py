class Cache:

    def __init__(self, tag_mask, tag_offset, index_mask, index_offset, associativity, sets, line_size):
        self.tag_mask   = tag_mask
        self.tag_offset = tag_offset
        self.index_mask = index_mask
        self.index_offset = index_offset

        self.associativity = associativity
        self.sets          = sets
        self.line_size     = line_size

        # Mirrors architecture of redstone implementation
        # i.e. each cache line has 4 blocks of data, each containing an upper and lower word
        self.data = [
            [[0x0000 for _ in range(line_size)] for _ in range(associativity)] for _ in range(sets)
        ]

    def get_tag_index(self, address):
        tag   = (address & self.tag_mask) >> self.tag_offset
        index = (address & self.index_mask) >> self.index_offset
        return tag, index
