from l1 import L1
from l2 import L2


class Core:

    def __init__(self):

        # Private cache structure:
        # L1 is split, private
        # L1i and L1d are 2-way set associative with 4 sets each
        # line size is 8 words, words are 16 bit
        # Total size: 8 * 2 * 8 = 256 Words / 512 Bytes

        # Note: L1i and L1d may contain shared blocks of data
        # Note: In redstone implementation, each line comprises contains 4 blocks of data,
        #       each with their own upper and lower word this results in the following address
        #       structure:

        # L1 address breakdown:
        # 11b tag, 2b idx, 2b block offset, 1b word offset
        # [00000000 000] [00] [00] [0]

        self.l1d = L1(0xFFE0, 5, 0x0018, 3,2, 4, 8)
        self.l1i = L1(0xFFE0, 5, 0x0018, 3,2, 4, 8)

        # L2 is unified, private
        # L2 is an eviction cache, it stores all cache lines evicted from L1
        # Note: L2 is not inclusive of L1
        # L2 is 2-way set associative with 16 sets
        # line size is 8 words, words are 16 bit
        # Total size: 16 * 2 * 8 = 256 Words / 512 Bytes

        # L2 address breakdown:
        # 9b tag, 4b idx, 3b unused
        # [00000000 0] [0000]  [000]

        self.l2  = L2(0xFF80, 8, 0x0078, 3, 2, 16, 8)
