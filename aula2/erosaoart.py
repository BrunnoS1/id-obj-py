import cv2
import os
import numpy as np

def carregar_imagens_pasta(pasta):
    ''' 
    argumento = nome da pasta 
    ex: carregar_imagens_pasta('img/')
    '''
    imagens = []
    for nomearq in os.listdir(pasta):
        img = cv2.imread(os.path.join(pasta,nomearq))
        if img is not None:
            imagens.append(img)
    return imagens

escolha = int(input('1 para olhos e 2 para face'))
if escolha == 1:
    classificador="haarcascade_eye_tree_eyeglasses.xml" # olhos
else:
    classificador="haarcascade_frontalface_default.xml" # face

face = cv2.CascadeClassifier(classificador)
imgs = carregar_imagens_pasta('img')
contador = 0

for imagem in imgs:
    cinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(cinza,scaleFactor=1.1,minNeighbors=5, minSize=(30,30)) # mínimo tamanho do objeto

    # Desenhando um retângulo na area identificada
    

    # Criando um elemento para a dilatação
    elem=np.ones((3,3),np.uint8)
    # Implementando a dilatação/erosao
    for iteration in (1,5,10):
        dilatacao =cv2.dilate(imagem,elem,iterations=iteration)
        for (x, y, w, h) in faces:
            cv2.rectangle(dilatacao, (x, y), (x+w, y+h), (0, 255, 210), 2)
            if escolha == 1:
                #para cada imagem exibir a distancia entre os olhos
                olho1 = faces[0][0]
                olho2 = faces[1][0]
                distancia = abs(olho2 - olho1)
                cv2.putText(dilatacao, f'{distancia:.0f}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
            else:
                #para cada imagem exibir o valor da diagonal
                diagonal = (w**2 + h **2)**0.5
                cv2.putText(dilatacao, f'{diagonal:.0f}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.imwrite(f"img_output/dilatacao{contador}-{iteration}.png", dilatacao)
        # cv2.imshow(f"Dilatacao iterations={iteration}", dilatacao)
        # cv2.waitKey()


        erosao=cv2.erode(imagem,elem,iterations=iteration)
        for (x, y, w, h) in faces:
            cv2.rectangle(erosao, (x, y), (x+w, y+h), (0, 255, 210), 2)
            if escolha == 1:
                #para cada imagem exibir a distancia entre os olhos
                olho1 = faces[0][0]
                olho2 = faces[1][0]
                distancia = abs(olho2 - olho1)
                cv2.putText(erosao, f'{distancia:.0f}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
            else:
                #para cada imagem exibir o valor da diagonal
                diagonal = (w**2 + h **2)**0.5
                cv2.putText(erosao, f'{diagonal:.0f}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.imwrite(f"img_output/erosao{contador}-{iteration}.png", erosao)
        # cv2.imshow(f"Erosao iterations={iteration}", erosao)
        # cv2.waitKey()
    
    contador += 1