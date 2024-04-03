import cv2
import numpy as np

# Carregando a imagem
img=cv2.imread('../aula1/img/coala.jpg')

# Transformando em escala de cinza
cinza=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Criando um elemento para a dilatação
elem=np.ones((3,3),np.uint8)

# Implementando a dilatação/erosao
for iteration in (1,5,10):
    dilatacao =cv2.dilate(cinza,elem,iterations=iteration)
    # cv2.imshow("Imagem com dilatação",img)
    # cv2.waitKey()
    cv2.imwrite(f"img_output/1coaladilatacao{iteration}.png", dilatacao)
    erosao=cv2.erode(cinza,elem,iterations=iteration)
    # cv2.imshow("Imagem com erosao",img)
    # cv2.waitKey()
    cv2.imwrite(f"img_output/1coalaerosao{iteration}.png", erosao)