import cv2
import numpy as np

def invert_colors_manual(img):
    ## Custom function to invert the colors of an image
    # @param : img
    img_inv = np.zeros(img.shape, dtype=np.uint8)
    for rowIdx in xrange(img.shape[0]):
        for colIdx in xrange(img.shape[1]):
            for chIdx in xrange(img.shape[2]):
                img_inv[rowIdx, colIdx, chIdx] = 255-img[rowIdx, colIdx, chIdx]

    return img_inv


def invert_colors_numpy(img):
    ## Function to invert the colors of an image
    # @param : img
    return (255 - img)

def invert_colors_opencv(img):
    ## Function to invert the colors of an image
    # @param : img
    return cv2.bitwise_not(img)


