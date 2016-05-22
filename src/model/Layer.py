import numpy as np


class layer:
    count = 0

    def __init__(self):
        layer.count += 1
        self.name = "Layer " + str(layer.count)
        self.pixelArray = np.zeros((400, 400))
        for row in range(400):
            for col in range(400):
                self.pixelArray = [255, 255, 255]
