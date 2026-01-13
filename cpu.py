from l3 import L3
from core import Core
from buffers import SharedBuffer

class CPU:

    def __init__(self, num_cores):
        # todo: 65KiB main mem, using file

        # Shared Cache Structure:
        # L3 is unified, shared
        # It is 4-way set associative with 128 sets
        # line size is 8 words, word size is 16 bit
        # Note: L3 is inclusive of all data in private caches

        # L3 Address breakdown:
        # 6b tag, 7b idx, 3b unused
        # [000000] [00 00000]  [000]

        self.l3 = L3(0xFC00, 10, 0x03F8, 3, 4, 128, 8)

        self.cores = [Core() for _ in range(num_cores)]


