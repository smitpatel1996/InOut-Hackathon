import Image
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import re
import numpy as np

image = cv2.imread("ac.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('temp.jpg', gray)
l1 = pytesseract.image_to_string(Image.open('temp.jpg'))
in1_list = l1.replace("\n"," ").split(" ")