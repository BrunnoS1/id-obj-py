# este programa identifica os pontos chaves para o reconhecimento facial

import math
import random
import cv2    # bibliotecas
import emuladlib

def calcula_distancia(ponto_a, ponto_b):
    return ((ponto_a[0] - ponto_b[0])**2 + (ponto_a[1] - ponto_b[1])**2 )**0.5

# emulando a dlib (passa o nome do arquivo e retorna os pontos em x e y para plotagem

arqs = ["mulher3","homem","palhaco"]
for item in arqs:
    (x,y)=emuladlib.emula(item)

    # Carregar a imagem
    image=cv2.imread(f"{item}.jpg")

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

    # lendo a posição dos olhos

    x36=x[36]     
    y36=y[36]
    x45=x[45]     
    y45=y[45]

    x0 = x[0]
    x1 = x[1]
    x2 = x[2]
    x3 = x[3]
    x4 = x[4]
    x5 = x[5]
    x6 = x[6]
    x7 = x[7]
    x8 = x[8]

    y0 = y[0]
    y1 = y[1]
    y2 = y[2]
    y3 = y[3]
    y4 = y[4]
    y5 = y[5]
    y6 = y[6]
    y7 = y[7]
    y8 = y[8]

    # dist01 = calcula_distancia((x0,y0),(x1,y1))
    # dist12 = calcula_distancia((x1,y1),(x2,y2))
    # dist23 = calcula_distancia((x2,y2),(x3,y3))
    # dist34 = calcula_distancia((x3,y3),(x4,y4))
    # dist45 = calcula_distancia((x4,y4),(x5,y5))
    # dist56 = calcula_distancia((x5,y5),(x6,y6))
    # dist67 = calcula_distancia((x6,y6),(x7,y7))
    # dist78 = calcula_distancia((x7,y7),(x8,y8))
    
    distx01 = abs(x0-x1)
    distx12 = abs(x1-x2)
    distx23 = abs(x2-x3)
    distx34 = abs(x3-x4)
    distx45 = abs(x4-x5)
    distx56 = abs(x5-x6)
    distx67 = abs(x6-x7)
    distx78 = abs(x7-x8)

    disty01 = abs(y0-y1)
    disty12 = abs(y1-y2)
    disty23 = abs(y2-y3)
    disty34 = abs(y3-y4)
    disty45 = abs(y4-y5)
    disty56 = abs(y5-y6)
    disty67 = abs(y6-y7)
    disty78 = abs(y7-y8)

    angulo01 = math.atan(disty01/distx01)*180/math.pi
    angulo12 = math.atan(disty12/distx12)*180/math.pi
    angulo23 = math.atan(disty23/distx23)*180/math.pi
    angulo34 = math.atan(disty34/distx34)*180/math.pi
    angulo45 = math.atan(disty45/distx45)*180/math.pi
    angulo56 = math.atan(disty56/distx56)*180/math.pi
    angulo67 = math.atan(disty67/distx67)*180/math.pi
    angulo78 = math.atan(disty78/distx78)*180/math.pi

    distv=((x51-x57)**2+(y51-y57)**2)**0.5  # calculando distância vertical e horizontal do lábio
    disth=((x48-x54)**2+(y48-y54)**2)**0.5
    disto=((x36-x45)**2+(y36-y45)**2)**0.5  # distância dos olhos

    # exibindo distâncias
    cv2.putText(image,"H="+str(disth),(1,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image,"V="+str(distv),(1,40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
    cv2.putText(image,"O="+str(disto),(1,60),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)

    # desenhando as retas
    cv2.line(image,(x36,y36),(x45,y45),(0,0,255),1)
    cv2.line(image,(x51,y51),(x57,y57),(0,255,0),1)
    cv2.line(image,(x48,y48),(x54,y54),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),1)
    cv2.line(image, (x0,y0),(x1,y1),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
    cv2.line(image, (x1,y1),(x2,y2),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
    cv2.line(image, (x2,y2),(x3,y3),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
    cv2.line(image, (x3,y3),(x4,y4),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
    cv2.line(image, (x4,y4),(x5,y5),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
    cv2.line(image, (x5,y5),(x6,y6),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
    cv2.line(image, (x6,y6),(x7,y7),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
    cv2.line(image, (x7,y7),(x8,y8),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)

    print(f"\nIMAGEM {item}\n")

    print(f"angulo01 = {angulo01:.2f}")
    print(f"angulo12 = {angulo12:.2f}")
    print(f"angulo23 = {angulo23:.2f}")
    print(f"angulo34 = {angulo34:.2f}")
    print(f"angulo45 = {angulo45:.2f}")
    print(f"angulo56 = {angulo56:.2f}")
    print(f"angulo67 = {angulo67:.2f}")
    print(f"angulo78 = {angulo78:.2f}")

    cv2.putText(image, f"angulo01 = {angulo01:.2f}",(1,80),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image, f"angulo12 = {angulo12:.2f}",(1,100),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image, f"angulo23 = {angulo23:.2f}",(1,120),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image, f"angulo34 = {angulo34:.2f}",(1,140),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image, f"angulo45 = {angulo45:.2f}",(1,160),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image, f"angulo56 = {angulo56:.2f}",(1,180),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image, f"angulo67 = {angulo67:.2f}",(1,200),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    cv2.putText(image, f"angulo78 = {angulo78:.2f}",(1,220),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
    
    # Exibir a imagem com os pontos-chave
    cv2.imshow("Face Keypoints",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


