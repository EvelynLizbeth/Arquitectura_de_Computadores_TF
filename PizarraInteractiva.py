import cv2
import numpy as np
#Captura de video por la entrada 2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#Rangos para la deteccion del color rojo 
RojoBajo = np.array([175, 100, 20], np.uint8)#ledsito rojo
RojoAlto = np.array([179, 255, 255], np.uint8)

# Colores para pintar
colorMorado = (255,113,168)#255,113,82
colorAmarilloClaro=(18,248,255)
colorRosado =(160,18,230)
colorAzul=(230,27,0)
colorCeleste =(223,230,0)
colorVerdeclaro=(174,255,227)
colorVerde =(107,228,89)

colorRojo =(42,38,255)
colorRosadoClaro=(255,166,249)
colorVerdeLimon=(72,255,173)
colorBeige=(215,241,255)
colorNaranja=(44,175,255)
blanco=(255,255,255)
#negro=(0,0,0)

colorCafe=(65,130,179)
colorPlomo=(179,179,179)

colorLimpiarPantalla = (255,238,164)

# Grosor de línea recuadros  (color a dibujar)
grosorMorado = 6
grosorAmarilloClaro=2
grosorRosado =2
grosorAzul=2
grosorCeleste =2
grosorVerdeclaro=2
grosorVerde =2
grosorRojo =2
grosorRosadoClaro=2
grosorVerdeLimon=2
grosorBeige=2
grosorNaranja=2
grosorBlanco=2
grosorCafe=2
#grosorPlomo=2

ListaGrosor =[grosorMorado,grosorAmarilloClaro,grosorRosado,grosorAzul,grosorCeleste,
grosorVerdeclaro,grosorVerde,grosorRojo,grosorRosadoClaro,grosorVerdeLimon,
grosorBeige,grosorNaranja,grosorBlanco,grosorCafe]
# Grosor de línea recuadros superior derecha (grosor del marcador para dibujar)
grosorPeque = 6
grosorMedio = 1
grosorGrande = 1

#Variables para el marcador / lápiz virtual -RojoLed 
color = colorMorado  # Color de entrada, y variable que asignará el color del marcador
grosor = 3 # Grosor que tendrá el marcador


x1 = None
y1 = None
imAux = None

while True:

    ret,frame = cap.read()
    if ret==False: break

    #frame = cv2.flip(frame,1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if imAux is None: imAux = np.zeros(frame.shape,dtype=np.uint8)
    # Cuadrados dibujados en la parte superior izquierda (representan el color a dibujar)

    cv2.rectangle(frame,(0,430),(50,479),colorMorado,grosorMorado)
    cv2.rectangle(frame,(53,430),(103,479),colorAmarilloClaro,grosorAmarilloClaro)
    cv2.rectangle(frame,(106,430),(156,479),colorRosado,grosorRosado)
    cv2.rectangle(frame,(159,430),(209,479),colorAzul,grosorAzul)
    cv2.rectangle(frame,(212,430),(262,479),colorCeleste ,grosorCeleste)
    cv2.rectangle(frame,(265,430),(315,479),colorVerdeclaro,grosorVerdeclaro)
    cv2.rectangle(frame,(318,430),(368,479),colorVerde,grosorVerde)
    #cv2.rectangle(frame,(318,430),(368,479),colorPlomo,grosorMorado)



    cv2.rectangle(frame,(0,376),(50,425),colorRojo,grosorRojo)
    cv2.rectangle(frame,(53,376),(103,425),colorRosadoClaro,grosorRosadoClaro)
    cv2.rectangle(frame,(106,376),(156,425),colorVerdeLimon,grosorVerdeLimon)
    cv2.rectangle(frame,(159,376),(209,425),colorBeige,grosorBeige)
    cv2.rectangle(frame,(212,376),(262,425),colorNaranja ,grosorNaranja)
    cv2.rectangle(frame,(265,376),(315,425),colorCafe,grosorCafe)
    cv2.rectangle(frame,(318,376),(368,425),blanco,grosorBlanco)
    
    #cv2.rectangle(frame,(318,376),(368,425),colorMorado,grosorMorado)
    
    # Cuadrados dibujados en la parte superior derecha (grosor del marcador para dibujar)
    cv2.rectangle(frame,(371,430),(421,479),(0,0,0),grosorPeque)
    cv2.circle(frame,(396,454),3,(0,0,0),-1)
    cv2.rectangle(frame,(421,430),(471,479),(0,0,0),grosorMedio)
    cv2.circle(frame,(446,454),7,(0,0,0),-1)
    cv2.rectangle(frame,(471,430),(521,479),(0,0,0),grosorGrande)
    cv2.circle(frame,(496,454),11,(0,0,0),-1)




    # Detección del color RojoLed
    maskRojo = cv2.inRange(frameHSV, RojoBajo, RojoAlto) 
    maskRojo = cv2.erode(maskRojo,None,iterations = 1)
    maskRojo = cv2.dilate(maskRojo,None,iterations = 2)
    maskRojo = cv2.medianBlur(maskRojo, 13)
    
    cnts,_ = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

    for c in cnts:
        area = cv2.contourArea(c)
        if area > 20:
            x,y2,w,h = cv2.boundingRect(c)
            x2 = x + w//2
            
            if x1 is not None:
                
                if 0 < x2 < 50 and 430 < y2 < 479:
                    color = colorMorado # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorMorado:
                                i=6
                        else :
                            i=2

                if 53 < x2 < 103 and 430 < y2 < 479:
                    color = colorAmarilloClaro # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorAmarilloClaro:
                            i=6
                        else :
                            i=2
                
                if 106 < x2 < 156 and 430 < y2 < 479:
                    color = colorRosado # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorRosado:
                            i=6
                        else :
                            i=2

                if 159 < x2 < 209 and 430 < y2 < 479:
                    color = colorAzul # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorAzul:
                            i=6
                        else :
                            i=2
                
                if 212 < x2 < 262 and 430 < y2 < 479:
                    color = colorCeleste # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorCeleste:
                            i=6
                        else :
                            i=2

                if 265 < x2 < 315 and 430 < y2 < 479:
                    color = colorVerdeclaro # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorVerdeclaro:
                            i=6
                        else :
                            i=2

                if 318 < x2 < 368 and 430 < y2 < 479:
                    color = colorVerde # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorVerde:
                            i=6
                        else :
                            i=2
                
                if 0 < x2 < 50 and 376 < y2 < 425:
                    color = colorRojo # Color del lápiz/marcador virtual 22222222222222
                    for i in ListaGrosor:
                        if i==grosorRojo:
                            i=6
                        else :
                            i=2


                if 53 < x2 < 103 and 376 < y2 < 425:
                    color = colorRosadoClaro # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorRosadoClaro:
                            i=6
                        else :
                            i=2
                
                if 106 < x2 < 156 and 376 < y2 < 425:
                    color = colorVerdeLimon # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorVerdeLimon:
                            i=6
                        else :
                            i=2

                if 159 < x2 < 209 and 376  < y2 < 425:
                    color = colorBeige # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorBeige:
                            i=6
                        else :
                            i=2
                
                if 212 < x2 < 262 and 376 < y2 < 425:
                    color = colorNaranja# Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorNaranja:
                            i=6
                        else :
                            i=2
                
                if 265 < x2 < 315 and 376 < y2 < 425:
                    color = colorCafe # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorCafe:
                            i=6
                        else :
                            i=2

                if 53 < x2 < 103 and 376 < y2 < 425:
                    color = blanco # Color del lápiz/marcador virtual
                    for i in ListaGrosor:
                        if i==grosorBlanco:
                            i=6
                        else :
                            i=2
                
                

                if 0 < y2 < 60 or 0 < y1 < 60 :
                    imAux = imAux
                else:
                    imAux = cv2.line(imAux,(x1,y1),(x2,y2),color,grosor)
            cv2.circle(frame,(x2,y2),grosor,color,7)
            x1 = x2
            y1 = y2
        else: 
            x1, y1 = None, None
    
    imAuxGray = cv2.cvtColor(imAux,cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(imAuxGray,10,255,cv2.THRESH_BINARY)
    thInv = cv2.bitwise_not(th)
    frame = cv2.bitwise_and(frame,frame,mask=thInv)
    frame = cv2.add(frame,imAux)
    
    #cv2.imshow('maskMorado', maskMorado)
    cv2.imshow('imAux',imAux)
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()