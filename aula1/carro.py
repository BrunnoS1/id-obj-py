import cv2

# classificador treinado para identificar carros
# contém as informações para classificar os carros
id_carros=cv2.CascadeClassifier('cars.xml')

# transformando o jpg em array (leitura da imagem)
carros=cv2.imread('img/car3.jpg')

# convertendo a imagem para tons de cinza
cinza=cv2.cvtColor(carros,cv2.COLOR_BGR2GRAY)

# detectando carros de vários tamanhos na imagem
localizados=id_carros.detectMultiScale(cinza,1.1,3)

# desenhando um retângulo em cada carro
for (x,y,w,h) in localizados:
    cv2.rectangle(carros,(x,y),(x+w,y+h),(0,255,0),2)
    # define regiao para borrar
    regiao = carros[y:y+h,x:x+w]
    # borra regiao da imagem
    regiao_filtro = cv2.GaussianBlur(regiao,(15,15),10)
    # devolve pra imagem a imagem com a regiao onde carro foi identificado borrada
    carros[y:y+h, x:x+w] = regiao_filtro

cv2.imshow('Identificando os carros',carros)
cv2.waitKey()