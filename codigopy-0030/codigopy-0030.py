# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
# ruta de la imagen
ruta_imagen= os.path.join(
    "img-original-0030",
    "mochila.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
jirafa = cv2.imread(ruta_imagen)
# print(mochila) muestra las matrices de la imagen
# Convertir de BGR a RGB color rojo COLOR_BGR2RGB
jir = cv2.cvtColor(jirafa, cv2.COLOR_BGR2RGB)
cv2.imshow("jir original 0030", jir)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # destruye todas las ventanas en memorias