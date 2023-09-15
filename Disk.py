class Disk:
    def __init__(self, value, next_disk=None):
        self.val = value
        self.next = next_disk