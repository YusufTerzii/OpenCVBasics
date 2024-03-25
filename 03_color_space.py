import cv2
import numpy as np

img = cv2.imread("01_OpenCVIntro/resim_okuma_gosterme_kaydetme/klon.jpg")

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("image",img)
cv2.imshow("imageRGB",img1)
cv2.imshow("imageGREY",img2)
cv2.imshow("imageHSV",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()