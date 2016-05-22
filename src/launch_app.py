import numpy as np
import cv2
from src.model import Layer
from src.controller import controller

if __name__ == "__main__":
    """ img is a BGR matrix! """

    img = cv2.imread("pikameth.jpg", cv2.IMREAD_UNCHANGED)

    cv2.imshow('Meth? Not even once!', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
