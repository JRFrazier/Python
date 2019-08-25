class SortedList(list):

    def __init__(self, value):
        self.value.sort() = value

        def append(self, value):
            super().append(value)
            self.sort()
