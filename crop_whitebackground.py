import os
import shutil
import sys
import numpy as np
from PIL import Image

file_extension = ["jpg", "bmp", "png"]

def getImageSizeWithoutWhitespace(img):
  width, height = img.size
  newX = width/2
  newY = height/2
  newWidth = width/2
  newHeight = height/2
  for x in range(0,width):
    for y in range(0,height):
      rgbValue = img.getpixel((x,y))
      if (rgbValue[0] < 230 and rgbValue[1] < 230 and rgbValue[2] < 230):
        if (x < newX):
          newX = x
        if (x > newWidth):
          newWidth = x
        if (y < newY):
          newY = y
        if (y > newHeight):
          newHeight = y
  return newX, newY, newWidth+1, newHeight+1

def getImageSizeWithoutBlackspace(img):
  width, height = img.size
  newX = width/2
  newY = height/2
  newWidth = width/2
  newHeight = height/2
  for x in range(0,width):
    for y in range(0,height):
      rgbValue = img.getpixel((x,y))
      if (rgbValue[0] > 25 and rgbValue[1] > 25 and rgbValue[2] > 25):
        if (x < newX):
          newX = x
        if (x > newWidth):
          newWidth = x
        if (y < newY):
          newY = y
        if (y > newHeight):
          newHeight = y
  return newX, newY, newWidth+1, newHeight+1

# Crop white background program in python

# Prerequisite:
# pip install numpy
# pip install Pillow

# Description
# The sample project provide you an example to crop white background and save to new image.
# Please put images in root directory.

for root, dirss, files in os.walk(".."):
  for filename in files:
    for ext in file_extension:
      if (filename.endswith("."+ext)):
        img = Image.open(filename)
        newX, newY, newWidth, newHeight = getImageSizeWithoutWhitespace(img)
        img = img.crop((newX,newY,newWidth,newHeight))
        img.save(filename.split(".")[0] + "_modified." + ext)
