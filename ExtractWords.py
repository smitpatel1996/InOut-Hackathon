import cv2
import numpy as np
import os, sys

def getWords(string):
	img = cv2.imread(string)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray,5)
	thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
	thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
	thresh = cv2.dilate(thresh,None,iterations = 3)
	thresh = cv2.erode(thresh,None,iterations = 1)
	cv2.imwrite('q1.png',thresh)
	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	cs = []
	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		if(w < 10 and h < 10):
			continue
		cs.append(cnt)	
	for q in cs:
		x,y,w,h = cv2.boundingRect(q)
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
	cv2.imwrite('q.png',img)        
getWords("right.png")