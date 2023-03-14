from typing import List
from gordot.shapes.shape import Shape

class DisplayFile:
    items: List[Shape] = []

    def append(self, item: Shape):
        self.items.append(item)

    def __getitem__(self, item):
        return self.items[item]