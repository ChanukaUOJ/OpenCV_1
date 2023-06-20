import cv2
img = cv2.imread("sample.png")
convertedImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("converted.png",convertedImage)
cv2.imshow("Befor Convertion",img)
cv2.imshow("After Convertion",convertedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
