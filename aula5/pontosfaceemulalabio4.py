# este programa identifica os pontos chaves para o reconhecimento facial

import cv2    # bibliotecas
import emuladlib
import math

def calcula_distancia(ponto_a, ponto_b):
    return ((ponto_a[0] - ponto_b[0])**2 + (ponto_a[1] - ponto_b[1])**2 )**0.5

# emulando a dlib (passa o nome do arquivo e retorna os pontos em x e y para plotagem
(x,y)=emuladlib.emula("palhaco")

# Carregar a imagem
image=cv2.imread("palhaco.jpg")

for i in range(68):  # 68 pontos-chave no rosto
    cv2.circle(image,(x[i],y[i]),2,(0,255,0),-1)
    # identificando cada ponto facial
    cv2.putText(image,str(i),(x[i],y[i]),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,255),1)

# lendo os pontos do labio para detectar sorriso ou boca aberta
x51=x[51]     # parte superior do lábio
y51=y[51]
x57=x[57]     # parte inferior do lábio
y57=y[57]

x48=x[48]     # extremo esquerdo do lábio
y48=y[48]
x54=x[54]     # extremo direito do lábio
y54=y[54]

# teste para verificar se está sorrindo, normal ou com a boca aberta
# apresentar na tela a distancia entre os pontos 36 e 45, a distancia entre os pontos 48 e 54
# e a distancia entre 51 e 57. desenhar retas ligando os pontos para exibir as distancias
# encontrar angulo entre a linha que liga pontos 8 e 0 e o angulo da linha que liga 8 e 16
# em relacao a horizontal ( usar math.atan )



# lendo a posição dos olhos
x36=x[36]     
y36=y[36]
x45=x[45]     
y45=y[45]

x0 = x[0]
y0 = y[0]
x8 = x[8]
y8 = y[8]
x16 = x[16]
y16 = y[16]

dist3645 = calcula_distancia((x36, y36),(x45, y45))
dist4854 = calcula_distancia((x48, y48),(x54, y54))
dist5157 = calcula_distancia((x51, y51),(x57, y57))

cv2.line(image, (x36,y36), (x45, y45), (255,0,0),2) # olhos
cv2.line(image, (x48,y48), (x54, y54), (255,0,0),2) # boca horizontal
cv2.line(image, (x51,y51), (x57, y57), (255,0,0),2) # boca vertical

# cv2.line(image, (x8,y8), (x0, y0), (0,0,255),2)
# cv2.line(image, (x8,y8), (x16, y16), (0,0,255),2)

dist80 = calcula_distancia((x8,y8), (x0, y0))
dist816 = calcula_distancia((x8,y8), (x16, y16))
cos80 = abs(x8-x0)/dist80
cos816 = abs(x8-x16)/dist816
sen80 = abs(y8-y0)/dist80
sen816 = abs(y8-y16)/dist816
angulo80 = (math.atan2(sen80,cos80))*180/math.pi
angulo816 = (math.atan2(sen816,cos816))*180/math.pi
#horizontal = ca
#dist = hip
# angulo80 = math.degrees(math.cos(cos80))
# angulo816 = math.degrees(math.cos(cos80))

cv2.putText(image, f"distancia = {dist3645:.2f}", (x36,y36-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0),1)
cv2.putText(image, f"distancia = {dist4854:.2f}", (x48,y48-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0),1)
cv2.putText(image, f"distancia = {dist5157:.2f}", (x51,y51-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0),1)
cv2.putText(image, f"angulo 8 0 = {angulo80:.2f}", (x0,y0-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0),1)
cv2.putText(image, f"angulo 8 16 = {angulo80:.2f}", (x16,y16-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0),1)

sorrindo = False
boca_aberta = False
if dist4854 > (dist3645*2)/3:
    #sorrindo
    cv2.putText(image, f"Sorrindo", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0),1)

else:
    if dist5157 > (dist4854*2)/3:
        #boca aberta
        cv2.putText(image, f"Boca aberta", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0),1)
    else:
        # nem boca aberta nem sorrindo = normal
        cv2.putText(image, f"Normal", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0),1)

# Exibir a imagem com os pontos-chave
cv2.imshow("Face Keypoints",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


