# Draw different geometric shapes using opencv
import numpy as np
import cv2
print(cv2.__version__)

# img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8)  #To make your own image!

# (img,point1,point2,color(BGR),thickness,lineType,shift)
# straight line-------------------
img = cv2.line(img,(0,0),(255,255),(255,0,0),3)
# arrowed line--------------------
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),3)
# rectangle-----------------------
# top left vertex coordinate --> x1,y1
# lower right vertex coordinate -->x2,y2
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),3)
# circle--------------------------
# (img,center,radius,color,thickness,lineType,shift)
img = cv2.circle(img,(447,63),63,(0,255,0),-1)
# Put text on image---------------
# (img,text,org,fontFace,fontScale,color,thickness,lineType,bottomLeftOrigin)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)


cv2.imshow('image', img)

cv2.waitKey(0)  # wait for closing event
cv2.destroyAllWindows() # destroy all windows created