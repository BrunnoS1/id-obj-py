import cv2

# XML de classificação
# classificador="haarcascade_eye_tree_eyeglasses.xml" # olhos
classificador="haarcascade_frontalface_default.xml" # face

# Classificador do xml da OpenCV para olhos
face = cv2.CascadeClassifier(classificador)

# Carregando a imagem
imagem = cv2.imread("img/katy.jpg")

# Convertendo para tons de cinza
cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

# Fazendo a detecção dos olhos
faces = face.detectMultiScale(cinza,scaleFactor=1.1,minNeighbors=5,
        minSize=(30,30)) # mínimo tamanho do objeto

# Desenhando um retângulo nos olhos
for (x, y, w, h) in faces:
    cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 210), 2)

# Exibindo a imagem
cv2.imshow("Detecção de olhos", imagem)
cv2.waitKey()