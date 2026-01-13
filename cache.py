class Cache:

    def __init__(self, tag_mask, tag_offset, index_mask, index_offset):
        self.tag_mask   = tag_mask
        self.tag_offset = tag_offset
        self.index_mask = index_mask
        self.index_offset = index_offset

    def get_tag_index(self, address):
        tag   = (address & self.tag_mask) >> self.tag_offset
        index = (address & self.index_mask) >> self.index_offset
        return tag, index
