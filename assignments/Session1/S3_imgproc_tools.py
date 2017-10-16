import cv2
import numpy as np

def invert_colors_manual(img):
    ## Custom function to invert the colors of an image
    # @param : img
    return False

img_gray = cv2.imread('cat.jpg', 0)

cv2.imshow("Test", img_gray)
cv2.waitKey()