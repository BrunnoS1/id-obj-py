import cv2
import numpy as np

# Carregando a imagem
img=cv2.imread('img/angelina.jpg')

# Transformando em escala de cinza
cinza=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Criando um elemento para a dilatação
elem=np.ones((3,3),np.uint8)

# Implementando a dilatação
dilatacao=cv2.dilate(cinza,elem,iterations=2)
# erosao=cv2.erode(cinza,elem,iterations=2)

# Exibindo a imagem com o efeito da dilatação
cv2.imshow("Imagem com dilatação",dilatacao)
# cv2.imshow("Imagem com dilatação",erosao)
cv2.waitKey()