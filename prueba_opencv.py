import numpy as np
import cv2
imagen = cv2.imread("/Users/ameliearroyo/Desktop/clueless-08x-cher-gty-jc-180521_hpMain_16x9_992.jpg")
# Mostrar la imagen
cv2.imshow("Ventana de OpenCV", imagen)
cv2.waitKey(0)  # Espera hasta que se presione una tecla
cv2.destroyAllWindows()  # Cierra la ventana
