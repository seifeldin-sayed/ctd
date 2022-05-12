import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading image
img = cv2.imread('IMG_3032.jpg')
img_final= cv2.imread("final product1.png")
# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray,120, 255, cv2.THRESH_BINARY)
#cv2.imshow('thresh', threshold)

# using a findContours() function
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0
t=c=q=l=0
# list for storing names of shapes
for contour in contours:

	# here we are ignoring first counter because
	# findcontour function detects whole image as shape
	# if i == 0:
	# 	i = 1
	# 	continue
	area= cv2.contourArea(contour)
	# cv2.approxPloyDP() function to approximate the shape
	if area>=500 and area<=50000:
		approx = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
		
		# using drawContours() function
		cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)
		

		# finding center point of shape
		#M = cv2.moments(contour)
		#if M['m00'] != 0.0:
			#x = int(M['m10']/M['m00'])
			#y = int(M['m01']/M['m00'])
		print(len(approx))
		# putting shape name at center of each shape
		if len(approx) == 3:
			#cv2.putText(img, 'Triangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
			t+=1
		elif len(approx) == 4:
			q+=1

		elif len(approx) <= 2:
			l+=1
		else:
			c+=1

# displaying the image after drawing contours
cv2.imshow('shapes', img)
cv2.putText(img_final,str(c),(50,40),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
cv2.putText(img_final,str(t),(50,110),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
cv2.putText(img_final,str(l),(50,200),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
cv2.putText(img_final,str(q),(50,280),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
cv2.imshow("image",img_final)
cv2.waitKey(0)
cv2.destroyAllWindows()