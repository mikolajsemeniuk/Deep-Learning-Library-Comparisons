import nnfs
import numpy as np
from nnfs.datasets import vertical_data
from datasets.base import Base


class Vertical(Base):
    def __init__(self, samples: int = 150, classes: int = 3) -> None:
        nnfs.init()
        self.x, self.y = vertical_data(samples = samples, classes = classes)
        self.y = np.expand_dims(self.y, 1)
