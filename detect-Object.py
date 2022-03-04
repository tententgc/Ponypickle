import cv2 
import numpy as np 

lower = np.array([15,150,20])
upper = np.array([35,255,255]) 

image = cv2.imread('img/test3.png') 

while True: 
    success, img  = image.read()
    
    