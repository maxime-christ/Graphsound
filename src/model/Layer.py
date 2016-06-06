import numpy as np


class Layer:
    count = 0

    def __init__(self, width, height):
        Layer.count += 1
        self.name = "Layer " + str(Layer.count)
        self.pixelArray = np.zeros((height, width, 3))
        for row in range(height):
            for col in range(width):
                self.pixelArray[row][col] = [255, 255, 255]
