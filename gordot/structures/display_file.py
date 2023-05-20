from typing import List
from copy import deepcopy
from gordot.structures import Vector, View

class DisplayFile:
    items: List['Shape'] = []

    def append(self, item: 'Shape'):
        self.items.append(item)

    def normalized_shapes(self, view: View):
        view_center = view.center()
        shapes = []

        for shape in self.items:
            y  = Vector(0, 1, 0)
            a  = view.up_vector().angle(y)

            shape = deepcopy(shape)
            shape.move(-view_center)
            shape.rotate(a)
            shapes.append(shape)

        return shapes
    
    def projected_shapes(self, origin: View, target: View) -> List['Shape']:
        a = self.normalized_shapes(origin)
        
        shapes = [
            shape.viewport_transform(origin.normalized(), target) 
            for shape in a
        ]
        
        return shapes
    
    def __getitem__(self, item):
        return self.items[item]