# aplicar o reconhecimento e filtro gaussiano em car1-5
# usar 3 valores pro filtro gaussiano (1,5,10)
import cv2

id_carros=cv2.CascadeClassifier('cars.xml')

carro1 = cv2.imread('img/car1.jpg')
carro2 = cv2.imread('img/car2.jpg')
carro3 = cv2.imread('img/car3.jpg')
carro4 = cv2.imread('img/car4.jpg')
carro5 = cv2.imread('img/car5.jpg')
carros = [carro1, carro2, carro3, carro4, carro5]


cinza1 = cv2.cvtColor(carro1,cv2.COLOR_BGR2GRAY)
cinza2 = cv2.cvtColor(carro2,cv2.COLOR_BGR2GRAY)
cinza3 = cv2.cvtColor(carro3,cv2.COLOR_BGR2GRAY)
cinza4 = cv2.cvtColor(carro4,cv2.COLOR_BGR2GRAY)
cinza5 = cv2.cvtColor(carro5,cv2.COLOR_BGR2GRAY)

localizados1=id_carros.detectMultiScale(cinza1,1.1,3)
localizados2=id_carros.detectMultiScale(cinza2,1.1,3)
localizados3=id_carros.detectMultiScale(cinza3,1.1,3)
localizados4=id_carros.detectMultiScale(cinza4,1.1,3)
localizados5=id_carros.detectMultiScale(cinza5,1.1,3)
localizados = [localizados1, localizados2, localizados3, localizados4, localizados5]

i = 0

for localizado in localizados:
    for variancia in (1,5,10):
        for (x,y,w,h) in localizado:
            cv2.rectangle(carros[i],(x,y),(x+w,y+h),(0,255,0),2)
            # define regiao para borrar
            regiao = carros[i][y:y+h,x:x+w]
            # borra regiao da imagem
            regiao_filtro = cv2.GaussianBlur(regiao,(15,15),variancia)
            # devolve pra imagem a imagem com a regiao onde carro foi identificado borrada
            carros[i][y:y+h, x:x+w] = regiao_filtro
            cv2.imshow(f'Identificando os carros {variancia}',carros[i])
            cv2.waitKey()
    i += 1