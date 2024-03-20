import cv2

# Carregando a imagem
img=cv2.imread('img/coala.jpg')

# Aplicando o filtro gaussiano com matriz 15x15
filtro=cv2.GaussianBlur(img,(15,15),3)

# exibindo a imagem com o filtro gaussiano
cv2.imshow("Filtro gaussiano",filtro)
cv2.waitKey()