import cv2

img = cv2.imread('leena.jpg',2)
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", bw_img)


rgb_img = cv2.cvtColor(bw_img, cv2.COLOR_GRAY2RGB)

cv2.imshow("Colored", rgb_img)
    

