import cv2
import os

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

# XML de classificação
escolha = int(input('1 para olhos e 2 para face'))
if escolha == 1:
    classificador="haarcascade_eye_tree_eyeglasses.xml" # olhos
else:
    classificador="haarcascade_frontalface_default.xml" # face

# Classificador do xml da OpenCV
face = cv2.CascadeClassifier(classificador)

imagens = carregar_imagens_pasta('img/')

for imagem in imagens:
    # Convertendo para tons de cinza
    cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

    # Fazendo a detecção dos olhos
    faces = face.detectMultiScale(cinza,scaleFactor=1.1,minNeighbors=5,
            minSize=(30,30)) # mínimo tamanho do objeto

    # Desenhando um retângulo na area identificada
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 210), 2)
        if escolha == 1:
            #para cada imagem exibir a distancia entre os olhos
            olho1 = faces[0][0]
            olho2 = faces[1][0]
            distancia = abs(olho2 - olho1)
            cv2.putText(imagem, f'{distancia:.0f}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        else:
            #para cada imagem exibir o valor da diagonal
            diagonal = (w**2 + h **2)**0.5
            cv2.putText(imagem, f'{diagonal:.0f}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

    # Exibindo a imagem
    cv2.imshow("Detecção de rostos", imagem)
    cv2.waitKey()