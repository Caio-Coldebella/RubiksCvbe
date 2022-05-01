import cv2
import numpy as np

def detectabordas(imgtratada,imgoriginal):
    #Aproxima os contornos por quadrilateros
    bordas = cv2.findContours(imgtratada, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)
    bordas = bordas[0] if len(bordas) == 2 else bordas[1]
    x,y,w,h = 0,0,0,0
    for borda in bordas:
        area = cv2.contourArea(borda)
        if(area > 5000):
            x, y, w, h = cv2.boundingRect(borda)
            cv2.rectangle(imgoriginal, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return [x,y,w,h]

 
def trata_imagem(path):
    img = cv2.imread(path)
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
    mask = cv2.inRange(imghsv,np.array([0,0,100]),np.array([255,255,255]))
    imgtratada = cv2.bitwise_and(img,img,mask=mask)
    imgtratada = cv2.cvtColor(imgtratada,cv2.COLOR_BGR2GRAY) # converte a imagem para grayscale
    return imgtratada

def main():
    path = "Assets/OF.jpg"
    img = cv2.imread(path)
    img = cv2.resize(img,(356,771))
    img_tratada = trata_imagem(path)
    img_tratada = cv2.resize(img_tratada,(356,771))
    coordenadas_face = detectabordas(img_tratada,img)
    print(coordenadas_face)
    cv2.imshow('tratada', img_tratada)
    cv2.imshow('Deteccao',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
main()
