import cv2
import numpy as np

# Carregando a imagem
img=cv2.imread('img/angelina.jpg')

# Transformando em escala de cinza
cinza=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Criando um elemento para a dilatação
elem=np.ones((3,3),np.uint8)

escolha = int(input("Digite 1 para dilatacao 2 para erosao"))

# Implementando a dilatação/erosao
if escolha == 1:
    img =cv2.dilate(cinza,elem,iterations=150)
    cv2.imshow("Imagem com dilatação",img)
    cv2.waitKey()
elif escolha == 2:
    erosao=cv2.erode(cinza,elem,iterations=2)
    cv2.imshow("Imagem com erosao",img)
    cv2.waitKey()