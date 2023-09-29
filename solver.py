import numpy as np
import cv2
from PIL import Image
from rembg import remove



img = cv2.imread('puzzles/ladybug.png')
channels = img.split()
print(channels.shape)


cv2.waitKey(0)