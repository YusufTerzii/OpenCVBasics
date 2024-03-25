import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("01_OpenCVIntro/resim_okuma_gosterme_kaydetme/klon.jpg")

cv2.imshow("img", img)

plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()