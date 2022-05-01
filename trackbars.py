import cv2
import numpy as np
RF=cv2.imread('Assets/RF.jpg')
RFhsv = cv2.cvtColor(RF,cv2.COLOR_BGR2HSV_FULL)
#hue: from 0 to 179, saturation and value: from 0 to 255
def empty(x):
  return x

cv2.namedWindow("TrackBars")
#cv2.resize("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,255,empty)
cv2.createTrackbar("Hue Max","TrackBars",255,255,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
  h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
  h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
  s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
  s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
  v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
  v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
  print(h_min,h_max,s_min,s_max,v_min,v_max)
  lower = np.array([h_min,s_min,v_min])
  upper = np.array([h_max,s_max,v_max])
  mask1 = cv2.inRange(RFhsv,lower,upper)
  mask = cv2.resize(mask1, (356,771))
  cv2.imshow('',mask)
  cv2.waitKey(1)