from dataclasses import dataclass

@dataclass
class View:
    xmin: int
    ymin: int
    xmax: int
    ymax: int

    def width(self):
        return self.xmax - self.xmin 

    def height(self):
        return self.ymax - self.ymin

    def __str__(self) -> str:
        return f"""View(
            [{self.xmin} {self.ymin}],
            [{self.xmax} {self.ymax}],
        )"""
