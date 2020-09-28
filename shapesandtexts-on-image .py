import cv2
import numpy as np

import matplotlib.pyplot as plt

##########creating an array of zeroes#############
blank_img = np.zeros(shape=(700,700,3),dtype=np.int16)

###########line##############
cv2.line(blank_img, pt1=(0,0),pt2=(700,700),color=(222,150,123),thickness=4)

####rectangle################
cv2.rectangle(blank_img, pt1=(384,5),pt2=(510,150),color=(0,255,0),thickness=10)

###############circle###########
cv2.circle(img=blank_img,center=(620,100),radius=20,color=(255,0,0),thickness=-1)

##############triangle###########
vertices = np.array([[500,300],[600,200],[700,300]],dtype=np.int32) ############two dimensional points################

#############since opencv in particular about dimensions so reshaping/casting vertices in three dimensions##################
points = vertices.reshape((-1,1,2))

cv2.polylines(blank_img , [points] , isClosed=True, color =(123,123,123), thickness=10)

##############triangle###########
vertices = np.array([[100,500],[150,400],[200,500]],dtype=np.int32) ############two dimensional points################

#############since opencv in particular about dimensions so reshaping/casting vertices in three dimensions##################
points = vertices.reshape((-1,1,2))

cv2.fillPoly(blank_img , [points] , color =(123,123,123))

########text#############

########### selecting font##############
font_style = cv2.FONT_HERSHEY_SIMPLEX 

cv2.putText(blank_img, text='Hello World!!!' , org=(10,690), fontFace= font_style, fontScale=3, color=(234,233,123), thickness=3, lineType=cv2.LINE_AA )

plt.imshow(blank_img)
plt.show()
   