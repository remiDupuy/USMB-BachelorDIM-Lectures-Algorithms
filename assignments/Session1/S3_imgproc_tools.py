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

def threshold_colors_numpy(img):
    ## Function to thresold the colors of an image
    # @param : img
    return (img>50).astype(np.uint8)*255

def threshold_colors_opencv(img):
    ## Function to thresold the colors of an image
    # @param : img
    return cv2.threshold(img, 127,200, cv2.THRESH_BINARY)[1]

###
img = cv2.imread('/home/remidupuy/Workspace/AlgoC/code/USMB-BachelorDIM-Lectures-Algorithms/assignments/Session1/cat.jpg')

imgThreshold = threshold_colors_opencv(img)
cv2.imshow('test', imgThreshold)
cv2.waitKey()


