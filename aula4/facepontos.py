# este programa identifica os pontos chaves para o reconhecimento facial

import cv2    # bibliotecas
import emuladlib

# emulando a dlib (passa o nome do arquivo e retorna os pontos em x e y para plotagem
(x,y)=emuladlib.emula("mulher")

# Carregar a imagem
image=cv2.imread("mulher.jpg")

for i in range(68):  # 68 pontos-chave no rosto
    cv2.circle(image,(x[i],y[i]),2,(0,255,0),-1)
    # identificando cada ponto facial
    cv2.putText(image,str(i),(x[i],y[i]),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,255),1)

x43 = x[43]
y43 = y[43]
x47 = x[47]
y47 = y[47]
x37 = x[37]
y37 = y[37]
x41 = x[41]
y41 = y[41]

dist_dir = ((x37-x41)**2 + (y37- y41)**2)**0.5
dist_esq = ((x43-x47)**2 + (y43- y47)**2)**0.5
cv2.putText(image,f"Distancia direita = {dist_dir}",(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
cv2.putText(image,f"Distancia esquerda = {dist_esq}",(0,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

if (dist_dir > dist_esq):
    cv2.putText(image,"Olho fechado: esquerdo",(0,60),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
else:
    cv2.putText(image, "Olho fechado: direito", (0,60),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        
# Exibir a imagem com os pontos-chave
cv2.imshow("Face Keypoints",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


