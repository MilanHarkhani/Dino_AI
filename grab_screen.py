# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:53:53 2019

@author: Milan
"""
import cv2
import numpy as np
from PIL import ImageGrab
import time


def grab_screen(_driver=None):
    screen = np.array(ImageGrab.grab(bbox=(40,180,440,400)))
    image = process_img(screen)
    cv2.imwrite('./Test_gray_canny.jpg', image) 
    time.sleep(2)
    return image

def process_img(image):
    #rescale the image
    image = cv2.resize(image,(0,0),fx=0.15,fy=0.10)
    cv2.imwrite('./Test_gray_resize.jpg', image) 
    time.sleep(2)
    #crop out dino agent
    image = image[2:38,10:50]
    cv2.imwrite('./Test_gray_resize_dino.jpg', image) 
    time.sleep(2)
    image = cv2.Canny(image,threshold1=100,threshold2=200)
    
    return image

def show_image(w_name,image):
    cv2.imshow(w_name,image)
    cv2.waitKey(1)
    
    
