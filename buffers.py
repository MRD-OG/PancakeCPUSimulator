
# Shared buffer: This interfaces with L3
class SharedBuffer:

    def __init__(self):
        pass

    def add_core_buffer(self, core_buffer):
        pass

    # todo: shared scheduler using priority and round robin


# Private buffer
class PrivateBuffer:

    def __init__(self):
        # todo: message format

        # OUTGOING:

        # (REQUEST, source, address)
        # request data from L3

        # (MODIFY, source, address, data)
        # modify L3 contents

        # (FORWARD, dest, address, data)
        # forward data to global bus for another core's request

        # (FLUSH, source, address, data)
        # force write back to L3

        # (FLUSH_TO_MAIN, address, data)
        # force write back to main mem

        # INCOMING:

        # (REQUEST, source, address)
        # request data from private cache for forwarding to another core

        # (FORWARD, address, data)
        # data received from other core

        # WIP: may use for invalidating specifically instruction or data
        # may be easier to just merge and apply blanket
        # (INVALIDATE_DATA, address)
        # (INVALIDATE_INSTRUCTION, address)

        # Fifo queues
        self.incoming = []
        self.outgoing = []

    def has_outgoing(self):
        return len(self.outgoing) > 0

    # Called by L3
    def consume_request(self):
        if self.has_outgoing():
            return self.outgoing.pop(0)
        else:
            # likely never chosen, shared buffer should check which things have requests
            return None

    def has_incoming(self):
        return len(self.incoming) > 0

    # Called by L2/L1
    def consume_incoming(self):
        if self.has_incoming():
            return self.incoming.pop(0)
        else:
            # likely never chosen, shared buffer should check which things have requests
            return None

    # L3 should be able to send messages to all cores
    # L3 should be able to receive requests from the buffer
    #   buffer.get_next_request()

    # L1 and L2 should be able to add a request
