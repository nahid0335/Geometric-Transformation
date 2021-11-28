# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 15:53:15 2021

@author: User
"""
import numpy as np
import cv2


def translateXY(img,tx,ty):
    rows,cols,_ = img.shape
    # Create the transformation matrix
    M = np.float32([[1,0,tx],
                    [0,1,ty]])
    
    # get the coordinates in the form of (0,0),(0,1)...(511,510),(511,511).
    # the shape is (2, rows*cols)
    orig_coord = np.indices((cols, rows)).reshape(2,-1)
    
    # stack the rows of 1 to form [x,y,1]
    orig_coord_f = np.vstack((orig_coord, np.ones(rows*cols)))
    
    #get the translated matrix
    transform_coord = np.dot(M, orig_coord_f)
    
    # Change into int type
    transform_coord = transform_coord.astype(int)
    
    # Keep only the coordinates that fall within the image boundary.
    indices = np.all((transform_coord[1]<rows, transform_coord[0]<cols, 
                      transform_coord[1]>=0, transform_coord[0]>=0), axis=0)
    
    # Create a zeros image and project the points
    output = np.zeros_like(img)
    output[transform_coord[1][indices], transform_coord[0][indices]] = img[orig_coord[1][indices], orig_coord[0][indices]]

    return output



def rotationTheta(img,theta):
    rows,cols,_ = img.shape
    # Create the transformation matrix
    angle = np.radians(theta)
    #center of image
    x0, y0 = ((cols-1)/2.0,(rows-1)/2.0)
    M = np.float32([[np.cos(angle), -np.sin(angle), x0*(1-np.cos(angle))+ y0*np.sin(angle)],
                  [np.sin(angle), np.cos(angle), y0*(1-np.cos(angle))- x0*np.sin(angle)]])
    
    # get the coordinates in the form of (0,0),(0,1)...(511,510),(511,511).
    # the shape is (2, rows*cols)
    orig_coord = np.indices((cols, rows)).reshape(2,-1)
    
    # stack the rows of 1 to form [x,y,1]
    orig_coord_f = np.vstack((orig_coord, np.ones(rows*cols)))
    
    #get the translated matrix
    transform_coord = np.dot(M, orig_coord_f)
    
    # Change into int type
    transform_coord = transform_coord.astype(int)
    
    # Keep only the coordinates that fall within the image boundary.
    indices = np.all((transform_coord[1]<rows, transform_coord[0]<cols, 
                      transform_coord[1]>=0, transform_coord[0]>=0), axis=0)
    
    # Create a zeros image and project the points
    output = np.zeros_like(img)
    output[transform_coord[1][indices], transform_coord[0][indices]] = img[orig_coord[1][indices], orig_coord[0][indices]]

    return output
    


def scaleXY(img,tx,ty):
    rows,cols,_ = img.shape
    # Create the transformation matrix
    M = np.float32([[tx,0,0],
                    [0,ty,0],
                    [0,0,1]])
    # get the coordinates in the form of (0,0),(0,1)...(511,510),(511,511).
    # the shape is (2, rows*cols)
    orig_coord = np.indices((cols, rows)).reshape(2,-1)
    
    # stack the rows of 1 to form [x,y,1]
    orig_coord_f = np.vstack((orig_coord, np.ones(rows*cols)))
    
    #get the translated matrix
    transform_coord = np.dot(M, orig_coord_f)
    
    # Change into int type
    transform_coord = transform_coord.astype(int)
    
    # Keep only the coordinates that fall within the image boundary.
    indices = np.all((transform_coord[1]<rows, transform_coord[0]<cols, 
                      transform_coord[1]>=0, transform_coord[0]>=0), axis=0)
    
    # Create a zeros image and project the points
    output = np.zeros_like(img)
    output[transform_coord[1][indices], transform_coord[0][indices]] = img[orig_coord[1][indices], orig_coord[0][indices]]
    
    return output




def sharingXY(img,tx,ty):
    rows,cols,_ = img.shape
    # Create the transformation matrix
    M = np.float32([[1,tx,0],
                    [ty,1,0],
                    [0,0,1]])
    # get the coordinates in the form of (0,0),(0,1)...(511,510),(511,511).
    # the shape is (2, rows*cols)
    orig_coord = np.indices((cols, rows)).reshape(2,-1)
    
    # stack the rows of 1 to form [x,y,1]
    orig_coord_f = np.vstack((orig_coord, np.ones(rows*cols)))
    
    #get the translated matrix
    transform_coord = np.dot(M, orig_coord_f)
    
    # Change into int type
    transform_coord = transform_coord.astype(int)
    
    # Keep only the coordinates that fall within the image boundary.
    indices = np.all((transform_coord[1]<rows, transform_coord[0]<cols, 
                      transform_coord[1]>=0, transform_coord[0]>=0), axis=0)
    
    # Create a zeros image and project the points
    output = np.zeros_like(img)
    output[transform_coord[1][indices], transform_coord[0][indices]] = img[orig_coord[1][indices], orig_coord[0][indices]]

    
    return output



img = cv2.imread('lena.jpg')
img = cv2.resize(img, (482,642))
cv2.imshow('input',img)

print(img.shape)

tx,ty = map(int, input("Enter x and y value for translation : ").split())

translatedImage = translateXY(img, tx, ty)

cv2.imshow('Translation',translatedImage)


theta = float(input("Enter Theta for rotation : "))
rotatedImage = rotationTheta(img, theta)

cv2.imshow('Rotation',rotatedImage)

tx,ty = map(float, input("Enter x and y value for scaling : ").split())

scaledImage = scaleXY(img, tx, ty)

cv2.imshow('Scaling',scaledImage)


tx,ty = map(float, input("Enter x and y value sharing : ").split())

sharedImage = sharingXY(img, tx, ty)

cv2.imshow('Sharing',sharedImage)


cv2.waitKey(0)
cv2.destroyAllWindows()