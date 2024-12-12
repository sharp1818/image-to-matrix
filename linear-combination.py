import cv2
import numpy as np

def combinar_lineal_imagenes(img1, img2, alpha):
    if img1.shape[:2] != img2.shape[:2]:
        if img1.shape[:2] < img2.shape[:2]:
            img1 = cv2.resize(img1, dsize=(img2.shape[1], img2.shape[0]))
        else:
            img2 = cv2.resize(img2, dsize=(img1.shape[1], img1.shape[0]))
    if img1.shape[2] != img2.shape[2]:
        if img1.shape[2] == 1 and img2.shape[2] == 3:
            img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
        elif img1.shape[2] == 3 and img2.shape[2] == 1:
            img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)


    img_combinada = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
    return img_combinada


img1 = cv2.imread('cat.jpg')
img2 = cv2.imread('icecream.jpg')
img_resultado = combinar_lineal_imagenes(img1, img2, 0.2)

cv2.imshow('Imagen Combinada', img_resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()