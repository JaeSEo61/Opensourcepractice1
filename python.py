import cv2
import numpy as np

img = cv2.imread('C:\img.jpg')


x = 50; y = 50
w = 50; h = 50
roi = img[y:y+h, x:x+w]

cv2.rectangle(roi,(0,0), (h-1, w-1), (0,255,0),5)

    
cv2.imshow("IMAGE", img)

key = cv2.waitKey(0)
cv2.waitKey()
cv2.destroyAllWindows()

