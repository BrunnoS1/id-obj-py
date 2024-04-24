import cv2

def distancia(centro1, centro2, x, y):
    distancias = []
    distancia1 = abs(((x - centro1[0])**2 + (y - centro1[1])**2)**(1/2))
    distancia2 = abs(((x - centro2[1])**2 + (y - centro2[1])**2)**(1/2))
    distancias.append(distancia1)
    distancias.append(distancia2)
    return distancias

# XML de classificacao
classificador="haarcascade_smile.xml"
classificador2="haarcascade_eye_tree_eyeglasses.xml"

# Classificação do xml da OpenCV para sorriso e olhos
face = cv2.CascadeClassifier(classificador)
face2 = cv2.CascadeClassifier(classificador2)

nomes=["../aula2/img/murphy.jpg","../aula2/img/gaga.jpg","../aula2/img/rock.jpg","../aula2/img/angelina.jpg","../aula2/img/dicaprio.jpg","../aula2/img/katy.jpg","../aula2/img/smith.jpg"]

for pessoa in nomes:
    
    # Carregando a imagem
    imagem = cv2.imread(pessoa)

    # Convertendo para tons de cinza
    cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

    # Fazendo a detecção do sorriso
    sorriso = face.detectMultiScale(
        cinza,
        scaleFactor=1.1,
        minNeighbors=500,
        minSize=(30,30) # mínimo tamanho do objeto
        )

    # Fazendo a detecção dos olhos
    olhos = face2.detectMultiScale(
        cinza,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30) # mínimo tamanho do objeto
        )

    # Desenhando um retângulo nos olhos
    for (x1, y1, w1, h1) in olhos:
        # Desenhando o retângulo
        cv2.rectangle(imagem, (x1, y1), (x1+w1, y1+h1), (0, 255, 210), 2)
        p1=olhos[0][0]  # posição dos olhos
        p2=olhos[1][0]

        centro1 = [(olhos[0][0]+ olhos[0][2]/2), (olhos[0][1]+ olhos[0][3]/2)]
        centro2 = [(olhos[1][0]+ olhos[1][2]/2), (olhos[1][1]+ olhos[1][3]/2)]

        dist_a = ((centro1[0] - centro2[0])**2 + (centro1[1] - centro2[1])**2)**(1/2)

        cv2.putText(imagem,f"dist. olhos={abs(dist_a):.2f}",(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
        # Desenhando um retângulo no sorriso (se houver um)
        for (x, y, w, h) in sorriso:
            # Desenhando o retângulo
            distancias = distancia(centro1, centro2, x, y)
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 210), 2)
            # cv2.putText(imagem,"sorriso="+str(w),(20,40),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(imagem,f"b olho2 boca={distancias[1]:.2f}",(20,80),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.putText(imagem,f"c olho1 boca={distancias[0]:.2f}",(20,60),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)

    # Exibindo a imagem
    cv2.imshow("Detecção de sorriso", imagem)
    cv2.waitKey(0)
