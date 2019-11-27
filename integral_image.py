# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:19:04 2019

@author: Valmir
"""

import cv2 as cv
import numpy as np

def summed_area_table(image):
    # Extracting the number os rows and columns
    height, width = image.shape
    
    # Creating the Summed-Area Table
    integral_image = np.zeros((height, width)).astype(int)
    
    for i in range(height):
        for j in range(width):
            sum_of_pixels = 0
            
            # The value of a pixel in the integral image is the sum of every pixel above and every left pixel OR
            # IntegralImage(x,y) = image(x,y) + IntegralImage(x,y-1) + IntegralImage(x-1,y) - IntegralImage(x-1,y-1)
            
            # Checking if the above and left pixels are not out of boundaries
            if (i - 1 >= 0):
                sum_of_pixels += integral_image[i - 1][j]
            
            if (j - 1 >= 0):
                sum_of_pixels += integral_image[i][j - 1]
                
            if (i - 1 >= 0 and j - 1 >= 0):
                sum_of_pixels -= integral_image[i - 1][j - 1]
            
            sum_of_pixels += image[i][j]
            integral_image[i][j] = sum_of_pixels
    
    return integral_image
            
            

if __name__ == "__main__":
    # Since an image is a matrix let's create one
    image = np.array([[31, 2, 4, 33, 5, 36],
             [12, 26, 9, 10, 29, 25],
             [13, 17, 21, 22, 20, 18],
             [24, 23, 15, 16, 14, 19],
             [30, 8, 28, 27, 11, 7],
             [1, 35, 34, 3, 32, 6]])
    
    integral_image = summed_area_table(image)