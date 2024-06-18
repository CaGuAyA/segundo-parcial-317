import cv2
import numpy as np

img1 = cv2.imread('./montania.jpg')
img2 = cv2.imread('./paisaje.jpg')

if img1 is None:
    print("Error al cargar la imagen montania.jpg")
    exit()

if img2 is None:
    print("Error al cargar la paisaje.jpg")
    exit()

width = max(img1.shape[1], img2.shape[1])
height = max(img1.shape[0], img2.shape[0])

img1_resized = cv2.resize(img1, (width, height))
img2_resized = cv2.resize(img2, (width, height))

sum_img = np.zeros_like(img1_resized, dtype=np.uint8)
sub_img = np.zeros_like(img1_resized, dtype=np.uint8)

for i in range(img1_resized.shape[0]): 
    for j in range(img1_resized.shape[1]):
        for k in range(img1_resized.shape[2]):
            sum_val = int(img1_resized[i, j, k]) + int(img2_resized[i, j, k])
            sum_img[i, j, k] = min(sum_val, 255)

            sub_val = int(img1_resized[i, j, k]) - int(img2_resized[i, j, k])
            sub_img[i, j, k] = max(sub_val, 0) 
            
cv2.imwrite('sum_image.jpg', sum_img)
cv2.imwrite('sub_image.jpg', sub_img)

cv2.imshow('Sum Image', sum_img)
cv2.imshow('Sub Image', sub_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
