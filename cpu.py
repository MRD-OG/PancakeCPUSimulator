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
        # Total capacity:

        # Note: Redstone implementation of L3 has an upper 4 and lower 4 words per cache line

        # L3 Address breakdown:
        # [6b tag] [7b idx]    [3b ignored]
        # [000000] [00 00000]  [000]

        # Initialise L3
        self.l3       = L3(0xFC00, 10, 0x03F8, 3, 4, 128, 8)

        # Create number of cores specified by constructor argument
        self.cores    = [Core() for _ in range(num_cores)]

        # Initialise shared buffer
        shared_buffer = SharedBuffer()
        self.l3.set_shared_buffer(shared_buffer)

        # Connect private buffers to shared buffer
        for core in self.cores:
            shared_buffer.add_core_buffer(core.get_private_buffer())
