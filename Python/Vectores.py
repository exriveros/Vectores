#***************************************************************
# Aplicacion Vectores
#           Fecha:      30/09/2026
#           Actualiza:  7/11/2026
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************

#EJEMPLOS:
# Crea Vectores 2D y les asigna proyecciones CVector(x,y):
#   a=CVector(4,1); b=CVector(4,-3); c=CVector(-3,1)

# Crea Vectores 2D y les asigna valores:
#   d=CVector(); d.Pol_g(4,78)              Expresión polar: magnitud 4 angulo polar 78°
#   d=CVector(); d.Azi_g(4,12)              Expresión azimutal: magnitud 4 angulo azimutal 12°

# Crea Vectores 3D y les asigna valores:
#   g=CVector3D(4, 3, 8)                    Proyecciones CVector3D(x,y,z)
#   g=CVector3D(); g.Cilindricas(4, 30, 2)  Proyecciones CVector3D (MagXY, AngPolar, z)
#   h=CVector3D(); h.Esfericas(4, 30, 62)   Proyecciones CVector3D (MagXY, AngPolar, AngZ)

# Genera una lista de vectores llamada Lv
#   Lv = [a,b,c,d]

# Representación gráfica de Vectores:
#   PloteaListVect(Lv)                              Presenta todos los vectores en el origen 2D
#   PloteaList3DVect(Lv)                            Presenta todos los vectores en el origen 3D
#   PloetaSumListVect(Lv)                           Presenta la suma de los vectores en el orden de la lista 2D
#   PloetaSum2ListVect(LVini,LVfin,VerResultante)   Presenta la suma 2 listas de vectores cerrado si Unir es True por defecto
#   PloteaSumList3DVect(Lv)                         Presenta la suma de los vectores en el orden de la lista 3D
#   PloteaSumVec(True,a,b,c)                        Presenta graficamente las combinaciones de sumar a, b y c    (a+b+c; a+c+b; b+a+c; b+c+a; c+a+b; c+b+c)
#   PloteaSumVec(True,a,b)                          Presenta graficamente las combinaciones de sumar a y b       (a+b; b+a)
#   PloteaSumVec(False,a,b,c)                       Presenta graficamente la suma a + b + c.    Usa el orden de entrada
#   PloteaSumVec(False,a,b)                         Presenta graficamente la suma a + b.        Usa el orden de entrada
#   PloteaSumVec(False,a,MulEsc(-1,b))              Presenta graficamente la suma a - b.        Usa el orden de entrada

# Presenta el vector 2D escrito:
#   VerVector(a)                            Presenta todas las expresiones del vector
#   VerVector(a,0)                          Muestra el vector usando vectores unitarios
#   VerVector(a,1)                          Muestra el vector usando proyecciones
#   VerVector(a,2)                          Muestra el vector usando expresión polar    (mag;<Dir Pol)
#   VerVector(a,3)                          Muestra el vector usando expresión azimutal (mag;<Dir Azi)

# Presenta el vector 2D escrito:
#   VerVector(a)                            Presenta todas las expresiones del vector
#   VerVector(a,0)                          Muestra el vector usando vectores unitarios
#   VerVector(a,1)                          Muestra el vector usando proyecciones
#   VerVector(a,2)                          Muestra el vector usando expresión polar    (mag;<Dir Pol)
#   VerVector(a,3)                          Muestra el vector usando expresión azimutal (mag;<Dir Azi)

# Presenta el vector 2D escrito:
#   VerVector(g)                            Presenta todas las expresiones del vector 3D
#   VerVector(g,0)                          Muestra el vector usando vectores unitarios
#   VerVector(g,1)                          Muestra el vector usando proyecciones
#   VerVector(g,2)                          Muestra el vector usando expresión cilíndricas polar    (mag;< Dir Pol; z)
#   VerVector(g,3)                          Muestra el vector usando expresión cilindricas azimutal (mag;< Dir Azi; z)
#   VerVector(g,4)                          Muestra el vector usando expresión esférica (mag;< Dir xyz; Dir z)

# Expresión de ángulo
#   Gms(a.DireccionPolar_g)                 Presenta la direccion Polar en grados usando grados, minutos y segundos.
#   Gms(a.DireccionAzimutal_g)              Presenta la direccion Azimutal en grados usando grados, minutos y segundos.

# Operaciones Vectoriales
#   f = MulEsc(2,a)                         Multiplicar el vector a por el escalar 2
#   g = DivEsc(2,a)                         Divide el vector a por el escalar 2
#   e = a - b - c                           Le restan al vector a los vectores b y c
#   e = MulEsc(-1,a+b+c+d)                  Equivale a decir e = -a-b-c
#   e = ProdPunto(a,b)                      Calcula el producto punto
#   m = ProdCruz(g,h)                       Calcula el vector resultante del producto cruz

# Operaciones con Vectores 2D:
#   a.Azi_g(mag, dirAzi_g)                  Asigna valores al vector usando coordenadas azimutales
#   a.Pol_g(mag, dirPol_g)                  Asigna valores al vector usando coordenadas polares
#   a.Rec(magx,magy)                        Asigna valores al vector usando proyecciones (x,y)
#   a.magnitud                              Regresa la magnitud del vector
#   a.x                                     Regresa la proyeccion en x
#   a.y                                     Regresa la proyeccion en y
#   a.DireccionAzimutal_g                   Regresa la direccion azimutal en grados
#   a.DireccionAzimutal_r                   Regresa la direccion azimutal en radianes
#   a.DireccionPolar_g                      Regresa la direccion polar en grados
#   a.DireccionPolar_r                      Regresa la direccion polar en radianes
#   a.ProdPuntoV(b)                         Regresa el producto punto con el vector b
#   a.Deflexion_Grad(b)                     Regresa el angulo de deflexión entre el vector a y el vector b en grados
#   a.Deflexion_Rad(b)                      Regresa el angulo de deflexión entre el vector a y el vector b en radianes
#   a.SentidoDeflex(b)                      Regresa el sentido de deflexion (izq = 1; der = -1; no hay = 0)
#   j = a.CosenosDirectores                 Regresa un vector con los cosenos directores (usar VerVector(j) para visualizar resultados)

# Operaciones con Vectores 3D:
#   g.Cilindricas(4,30,2)                   Asigna valores al vector usando (magXY, AngPolarXY, ElevacionZ)
#   g.Esfericas(4,30,60)                    Asigna valores al vector usando (magXY, AngPolarXY, AnguloZ)
#   g.Rec(3,2,4)                            Asigna valores al vector usando proyecciones (MagX,MagY,MagZ)
#   g.magnitudxy                            Regresa la magnitud del vector en el plano xy 
#   g.magnitudxyz                           Regresa la magnitud del vector sistema esférico o xyz
#   g.x                                     Regresa la proyeccion en x
#   g.y                                     Regresa la proyeccion en y
#   g.z                                     Regresa la proyeccion en y
#   g.DireccionAzimutal_g                   Regresa la direccion azimutal en grados
#   g.DireccionAzimutal_r                   Regresa la direccion azimutal en radianes
#   g.DireccionPolar_g                      Regresa la direccion polar en grados
#   g.DireccionPolar_r                      Regresa la direccion polar en radianes
#   g.DireccionZ_g                          Regresa el angulo con Z en grados
#   g.DireccionZ_r                          Regresa el angulo con Z en radianes
#   g.ProdPuntoV(b)                         Regresa el producto punto con el vector b
#   m = g.CosenosDirectores                 Regresa un vector con los cosenos directores (usar VerVector(j) para visualizar resultados)

#**********************************************************************************************************************************




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#        CARGA LAS LIBRERÍAS A UTILIZAR
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import math
import matplotlib.pyplot as plt
#----------------------------------------------------------------
# Carga las librerias OOP de vectores 2D y 3D
from CVector import CVector
from CVector3D import CVector3D

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#        FUNCIONES QUE PERMITEN VER INFORMACION (2 DATOS) EN POLAR, AZIMUTAL O COORDENADAS (X;Y)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def Polar(x, y):
    Vector = CVector()     # define la variable como vector 2D
    Vector.Rec(x,y)        # inicializa el vector con informacion vectorial polar
    print("( {:8.2f}".format(Vector.magnitud) + " ;< " + "{:8.4f}".format(Vector.Direccion_g) + "° )") # presenta los resultados

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Azimutal(x, y):
    Vector = CVector()     # define la variable como vector 2D
    Vector.Rec(x,y)        # inicializa el vector con informacion vectorial polar    
    print("( {:8.2f}".format(Vector.magnitud) + " ;< " + "{:8.4f}".format(Vector.DireccionPolar_g) + "° )") # presenta los resultados

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Rectangular(mag, DirPol_g):
    Vector = CVector()            # define la variable como vector 2D
    Vector.Pol_g(mag,DirPol_g)    # inicializa el vector con informacion vectorial polar
    print("( {:11.4f}".format(Vector.x) + "; " + "{:11.4f}".format(Vector.y) + " )") # presenta los resultados

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Rectangular_Azi(mag, DirAzi_g):
    Vector = CVector()          # define la variable como vector 2D
    Vector.Azi_g(mag,DirAzi_g)  # inicializa el vector con informacion vectorial azimutal
    print("( {:11.4f}".format(Vector.x) + " ;< " + "{:11.4f}".format(Vector.y) + " )") # presenta los resultados

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   FUNCIONES OPERACIONES VECTORIALES, REQUIEREN 2 VECTORES O ESCALAR Y VECTOR
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def MulEsc(ValEscalar, Vector):
    if isinstance(Vector,CVector):
        #----------------------------------------------------------------
        # define el vector R y lo inicializa multiplicando por el escalar 
        R = CVector(ValEscalar * Vector.x, ValEscalar * Vector.y)
        return R
    elif isinstance(Vector,CVector3D):
        R = CVector3D(round(ValEscalar * Vector.x, 13), round(ValEscalar * Vector.y, 13), round(ValEscalar * Vector.z, 13))
        return R
    else:
        return 0

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def DivEsc(ValEscalar, Vector):
    if isinstance(Vector,CVector):
        #----------------------------------------------------------------
        # define el vector R y lo inicializa multiplicando por el escalar 
        R = CVector(Vector.x / ValEscalar, Vector.y / ValEscalar)
        return R
    elif isinstance(Vector,CVector3D):
        R = CVector3D(round(Vector.x / ValEscalar, 13), round(Vector.y / ValEscalar, 13), round(Vector.z / ValEscalar, 13))
        return R
    else:
        return 0
        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdPunto(VectorA, VectorB):
    A=VectorA
    B=VectorB
    if (isinstance(VectorA,CVector3D) and isinstance(VectorB,CVector3D)):

        #----------------------------------------------------------------
        # calcula el producto punto de los vectores, con resultado escalar 
        R = (A.x * B.x) + (A.y * B.y) + (A.z * B.z)

        return R
    elif (isinstance(VectorA,CVector) and isinstance(VectorB,CVector)):
        R = (A.x * B.x) + (A.y * B.y)

        return round(R,13)
    else:
        return 0

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdCruz(VectorA,VectorB):
    if (isinstance(VectorA,CVector3D) and isinstance(VectorB,CVector3D)):
        A=VectorA
        B=VectorB
        R=CVector3D(0,0,0)
        #----------------------------------------------------------------
        # calcula el producto cruz de los vectores, con resultado vector 
        R.x = round((+1) * (A.y * B.z - A.z * B.y), 13)
        R.y = round((-1) * (A.x * B.z - A.z * B.x), 13)
        R.z = round((+1) * (A.x * B.y - A.y * B.x), 13)
    elif (isinstance(VectorA,CVector) and isinstance(VectorB,CVector)):
        R.z = round((+1) * (A.x * B.y - A.y * B.x), 13)
    else:
        R.x = 0

    return R
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def DeflexionRad(VectorA,VectorB):
    C = CVector(1,2);
    
    if (isinstance(VectorA,CVector) and isinstance(VectorB,CVector)):
        #----------------------------------------------------------------
        # calcula la deflexion entre los vectores (ángulo entre ellos)
        R = VectorA.Deflexion_Rad(VectorB)
    elif (isinstance(VectorA,CVector3D) and isinstance(VectorB,CVector3D)):
        R =  VectorA.Deflexion_RadXY
    else:
        R = 0

    return R

def DeflexionGrad(VectorA,VectorB):
    if (isinstance(VectorA,CVector) and isinstance(VectorB,CVector)):
        S = DeflexionRad(VectorA,VectorB) * 180.0 / 3.14159265358979323846264
    else:
        S = 0
    return round(S,8)

def AdicionVectorDeflexion(VectAnterior, Longitud, Deflexion, Referencia):
    print('hola')
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     MUESTRA UN ÁNGULO EXPRESADO EN GRADOS SEPARADO EN GRADOS, MINUTOS Y SEGUNDOS.
def Grd_Gms(GrdsDec):
    GrdsDec = GrdsDec if GrdsDec >= 0 else (360 + GrdsDec)
    G=int(GrdsDec)
    M=int((GrdsDec-G)*60.0)
    S=round((GrdsDec-G-M/60.0)*3600,2)
    if S == 60:
        S = 0.0
        M = int(M+1)
        if M == 60:
            M = int(0)
            G = int(G+1)
    G = G % 360    
    print("Ángulo: {:2d}".format(G) + "° {:02d}".format(M)+"\' {:05.2f}".format(S) + "\"")

def Gms_Grd(Grados: int, minutos: int, segundos:float):
    Signo= -1 if Grados < 0 else 1    
    Grados   = abs(Grados)
    minutos  = abs(minutos)
    segundos = abs(segundos)
    return Signo * (Grados + minutos / 60.0 + segundos / 3600.0)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     DIBUJA LOS VECTORES EN GRÁFICA
#

def PloteaListVect(ListaVectores):
    AnchoFlechaEje = 0.1
    x = [0]
    y = [0]

    fig = plt.figure()
    
    ax = fig.add_subplot()
    
    for Vec in ListaVectores:
        print("( " + str(Vec.x) +"; "+ str(Vec.y) + " )")
        ax.quiver(0,0,Vec.x,Vec.y, color = 'r', angles='xy', scale_units='xy',scale=1,)
        x.append(Vec.x)
        y.append(Vec.y)
        

    ax.set_xlim(min(x)-1,max(x)+1)
    ax.set_ylim(min(y)-1,max(y)+1)

    plt.grid(visible = 'true', which = 'both', axis = 'both', color = 'b')
    plt.xlabel('Este (x-->)')
    plt.ylabel('Norte (y-->)')
    plt.show()

def PloteaList3DVect(ListaVectores):
    AnchoFlechaEje = 0.1
    fig = plt.figure()
    x=[]
    y=[]
    z=[]
    ax = fig.add_subplot(111, projection = "3d")

    plt.quiver(-1,0,0,3,0,0, color = 'b', arrow_length_ratio = 0.3)
    plt.quiver(0,-1,0,0,3,0, color = 'b', arrow_length_ratio = 0.3)
    plt.quiver(0,0,-1,0,0,3, color = 'b', arrow_length_ratio = 0.3)
    
    for Vec in ListaVectores:
        #print("( " + str(Vec.x) +"; "+ str(Vec.y) + " )")
        x.append(Vec.x);y.append(Vec.y);z.append(Vec.z)
        plt.quiver(0,0,0,Vec.x,Vec.y, Vec.z,color = 'r', arrow_length_ratio = 0.2)

    ax.set_xlim(min(x)-1,max(x)+1)
    ax.set_ylim(min(y)-1,max(y)+1)
    ax.set_zlim(min(z)-1,max(z)+1)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.title("Lista Vectores 3D")
    
    plt.show()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     DIBUJA LA SUMA DE VECTORES EN GRÁFICA TOMANDO EL ORDEN DE LOS VECTORES EN LA LISTA
#

def PloteaSumList3DVect(ListaVectores):
    AnchoFlechaEje = 0.1
    x = [0]
    y = [0]
    z = [0]
    i = int(0)

    for Vec in ListaVectores:
        x.append(Vec.x + x[i])
        y.append(Vec.y + y[i])
        z.append(Vec.z + z[i])
        i += int(1)

    fig = plt.figure()

    ax = fig.add_subplot(111, projection = "3d")

    plt.quiver(-1,0,0,3,0,0, color = 'b', arrow_length_ratio = 0.3)
    plt.quiver(0,-1,0,0,3,0, color = 'b', arrow_length_ratio = 0.3)
    plt.quiver(0,0,-1,0,0,3, color = 'b', arrow_length_ratio = 0.3)

    for j in range(0,len(x)-1):        
        Tmp=CVector3D(x[j+1]-x[j],y[j+1]-y[j],z[j+1]-z[j])
        plt.quiver(x[j],y[j],z[j],Tmp.x,Tmp.y, Tmp.z,color = 'r', arrow_length_ratio = 1/Tmp.magnitudxyz)

    ax.set_xlim(min(x)-1,max(x)+1)
    ax.set_ylim(min(y)-1,max(y)+1)
    ax.set_zlim(min(z)-1,max(z)+1)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.title("Suma Vectores 3D (orden lista)")

    plt.show()

def PloteaSumListVect(ListaVectores):
    AnchoFlechaEje = 0.1
    x = [0]
    y = [0]
    i = int(0)

    for Vec in ListaVectores:
        x.append(Vec.x + x[i])
        y.append(Vec.y + y[i])
        i += int(1)

    plt.arrow(-1,0,3,0, width = AnchoFlechaEje)
    plt.arrow(0,-1,0,3, width = AnchoFlechaEje)

    for j in range(0,len(x)-1):
        print(str(x[j]) +";"+ str(y[j]) + " --- " + str(x[j+1]-x[j]) + ";" + str( y[j+1]-y[j]))
        Tmp=CVector(x[j+1]-x[j],y[j+1]-y[j])
        plt.arrow(x[j],y[j],Tmp.x-0.5*math.cos(Tmp.DireccionPolar_r),Tmp.y-0.5*math.sin(Tmp.DireccionPolar_r), width = 0.1, color = 'r')

    plt.plot(x,y,color = 'b')

    plt.grid(visible = 'true', which = 'both', axis = 'both', color = 'b')
    plt.xlabel('Este (x-->)')
    plt.ylabel('Norte (y-->)')
    plt.show()

def PloteaSum2ListVect(ListaVect_PosIni,ListaVect_PosFin, Unir: bool = True):
    AnchoFlechaEje = 0.1
    fin_a=CVector()
    fin_b=CVector()

    x = [0]
    y = [0]
    i = int(0)
    
    for Vec in ListaVect_PosIni:
        x.append(Vec.x + x[i])
        y.append(Vec.y + y[i])
        i += int(1)

    fig = plt.figure()
    ax = fig.add_subplot()
    
    
    plt.arrow(-1,0,3,0, width = AnchoFlechaEje)
    plt.arrow(0,-1,0,3, width = AnchoFlechaEje)

    for j in range(0,len(x)-1):
        Tmp=CVector(x[j+1],y[j+1])
        V1 = plt.quiver(x[j],y[j],Tmp.x-x[j],Tmp.y-y[j], color = 'r', angles='xy', scale_units='xy',scale=1,)
        if j==0:
            V1.set_label('RutaPosIni')
        fin_a.x += Tmp.x - x[j]
        fin_a.y += Tmp.y - y[j]
        j += int(1)

    AnchoFlechaEje = 0.1
    x1 = [0]
    y1 = [0]
    i = int(0)

    for Vec1 in ListaVect_PosFin:
        x1.append(Vec1.x + x1[i])
        y1.append(Vec1.y + y1[i])
        i += int(1)

    for j in range(0,len(x1)-1):
        Tmp1=CVector(x1[j+1],y1[j+1])
        V2 = plt.quiver(x1[j],y1[j],Tmp1.x - x1[j],Tmp1.y - y1[j], color = 'b', angles='xy', scale_units='xy',scale=1,)
        if j==0:
            V2.set_label('RutaPosFin')
        fin_b.x += Tmp1.x - x1[j]
        fin_b.y += Tmp1.y - y1[j]
        j += int(1)
    

    R=CVector(fin_b.x - fin_a.x,fin_b.y - fin_a.y)

    if Unir == True:
        plt.quiver(fin_a.x,fin_a.y, R.x, R.y, color = 'g', angles='xy', scale_units='xy',scale=1,label='Result')
    
    xmin = (min(x) if min(x1)>min(x) else min(x1)) - 2
    ymin = (min(y) if min(y1)>min(y) else min(y1)) - 2
    xmax = (max(x) if max(x1)<max(x) else max(x1)) + 2
    ymax = (max(y) if max(y1)<max(y) else max(y1)) + 2

    fig.text(0,0,"Resultante =" + ( "" if R.x > 0 else "(") + "{:8.4f}".format(R.x) + ( "" if R.x > 0 else ")") + " i\u0302 + " +  
             ( "" if R.y > 0 else "(") + "{:8.4f}".format(R.y) + ( "" if R.y > 0 else ")") + " j\u0302" +
             " = (" + str(round(R.magnitud,2)) + " ;\u2221 " + str(round(R.DireccionPolar_g,4)) + "° )")

    DesplzTx = 0.25
    plt.text(fin_a.x+DesplzTx, fin_a.y+DesplzTx,"PosIni", color='m', size = 'x-large', style = 'italic',ha = 'center',weight = 'bold')
    plt.text(fin_b.x+DesplzTx, fin_b.y+DesplzTx,"PosFin", color='m', size = 'x-large', style = 'italic',ha = 'center',weight = 'bold')
    
    ax.set_xlim(xmin,xmax)
    ax.set_ylim(ymin,ymax)

    ax.legend()
    
    plt.grid(visible = 'true', which = 'both', axis = 'both', color = 'y')
    plt.xlabel('Este (x-->)')
    plt.ylabel('Norte (y-->)')
    plt.show()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     DIBUJA VECTORES EN 2 DIMENSIONES SUMANDOLOS CON LA ALTERNATIVA DE SUMAS (APLICANDO DISTRIBUTIVA A LAS SUMAS)
def PloteaSumVec(Ver_Alternativas: bool = False, VectA: CVector = CVector(1,1), VectB = None, VectC = None):
    AnchoFlechaEje = 0.1
    if isinstance(VectA,CVector) and isinstance(VectB,CVector) and isinstance(VectC,CVector):
        x = [0, VectA.x, VectA.x + VectB.x, VectA.x + VectB.x + VectC.x]
        y = [0, VectA.y, VectA.y + VectB.y, VectA.y + VectB.y + VectC.y]

        plt.plot(x,y)

        plt.arrow(0,0,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')
        plt.arrow(VectA.x,VectA.y,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')
        plt.arrow(VectA.x+VectB.x,VectA.y+VectB.y,VectC.x-0.5*math.cos(VectC.DireccionPolar_r),VectC.y-0.5*math.sin(VectC.DireccionPolar_r), width = 0.1, color = 'y')

        if Ver_Alternativas == True:
            plt.arrow(0,0,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')
            plt.arrow(VectB.x,VectB.y,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')
            plt.arrow(VectA.x+VectB.x,VectA.y+VectB.y,VectC.x-0.5*math.cos(VectC.DireccionPolar_r),VectC.y-0.5*math.sin(VectC.DireccionPolar_r), width = 0.1, color = 'y')

            plt.arrow(0,0,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')
            plt.arrow(VectB.x,VectB.y,VectC.x-0.5*math.cos(VectC.DireccionPolar_r),VectC.y-0.5*math.sin(VectC.DireccionPolar_r), width = 0.1, color = 'y')
            plt.arrow(VectB.x+VectC.x,VectB.y+VectC.y,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')

            plt.arrow(0,0,VectC.x-0.5*math.cos(VectC.DireccionPolar_r),VectC.y-0.5*math.sin(VectC.DireccionPolar_r), width = 0.1, color = 'y')
            plt.arrow(VectC.x,VectC.y,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')
            plt.arrow(VectA.x+VectC.x,VectA.y+VectC.y,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')

            plt.arrow(0,0,VectC.x-0.5*math.cos(VectC.DireccionPolar_r),VectC.y-0.5*math.sin(VectC.DireccionPolar_r), width = 0.1, color = 'y')
            plt.arrow(VectC.x,VectC.y,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')
            plt.arrow(VectB.x+VectC.x,VectB.y+VectC.y,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')

            plt.arrow(0,0,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')
            plt.arrow(VectA.x,VectA.y,VectC.x-0.5*math.cos(VectC.DireccionPolar_r),VectC.y-0.5*math.sin(VectC.DireccionPolar_r), width = 0.1, color = 'y')
            plt.arrow(VectA.x+VectC.x,VectA.y+VectC.y,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')

        plt.arrow(-1,0,3,0, width = AnchoFlechaEje)
        plt.arrow(0,-1,0,3, width = AnchoFlechaEje)

        plt.grid(visible = 'true', which = 'both', axis = 'both', color = 'b')
        plt.xlabel('Este (x)')
        plt.ylabel('Norte (y)')
        plt.title("Suma Combinada de 3 Vectores")
        plt.show()
    elif isinstance(VectA,CVector) and isinstance(VectB,CVector) and VectC == None:
        x = [0, VectA.x, VectA.x + VectB.x]
        y = [0, VectA.y, VectA.y + VectB.y]

        plt.plot(x,y)

        plt.arrow(0,0,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')
        plt.arrow(VectA.x,VectA.y,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')

        if Ver_Alternativas == True:
            plt.arrow(0,0,VectB.x-0.5*math.cos(VectB.DireccionPolar_r),VectB.y-0.5*math.sin(VectB.DireccionPolar_r), width = 0.1, color = 'b')
            plt.arrow(VectB.x,VectB.y,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')

        plt.arrow(-1,0,3,0, width = 0.05, color = 'm')
        plt.arrow(0,-1,0,3, width = 0.05, color = 'm')

        plt.grid(visible = 'true', which = 'both', axis = 'both', color = 'b')
        plt.xlabel('Este (x)')
        plt.ylabel('Norte (y)')
        plt.title("Suma Combinada de 2 Vectores")
        plt.show()
    elif isinstance(VectA,CVector) and VectB == None and VectC == None:
        x = [0, VectA.x]
        y = [0, VectA.y]

        plt.plot(x,y)

        plt.arrow(0,0,VectA.x-0.5*math.cos(VectA.DireccionPolar_r),VectA.y-0.5*math.sin(VectA.DireccionPolar_r), width = 0.1, color = 'r')

        plt.arrow(-1,0,3,0, width = 0.05, color = 'm')
        plt.arrow(0,-1,0,3, width = 0.05, color = 'm')

        plt.grid(visible = 'true', which = 'both', axis = 'both', color = 'b')
        plt.xlabel('Este (x)')
        plt.ylabel('Norte (y)')
        plt.title("Muestra 1 Vector")
        plt.show()
    else:
        print("Error: no definió vectores")


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     VER VECTORES DE 2 DIMENSIONES O 3 DIMENSIONES MEDIANTE DIFERENTES SISTEMAS DE REFERENCIA
#        - vectores unitarios
#        - proyecciones
#        - polares
#        - azimutales
#        - cilindricas con polares
#        - cilindricas con azimutales
#        - esféricas
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def VerVector(Vector, i=None): #imprime el vector usando diferentes referencias
    if isinstance(Vector,CVector):
        if i is None:
            print("0). Por Vectores Unitarios   {:10.4f}".format(Vector.x) + " " + chr(238)+" + " + "{:10.4f}".format(Vector.y) + " " + chr(309))
            print("1). Por Proyecciones       ( {:10.4f}".format(Vector.x) + " ; " + "{:10.4f}".format(Vector.y) + " )")
            print("2). Por Vectorial Polar    ( {:8.2f}".format(Vector.magnitud) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° )")
            print("3). Por Vectorial Azimutal ( {:8.2f}".format(Vector.magnitud) + " ;< " + "{:11.4f}".format(Vector.DireccionAzimutal_g) + "° )")
        elif i == 0:
            print("Por Vectores Unitarios   {:10.4f}".format(Vector.x) + " i + " + "{:10.4f}".format(Vector.y) + " j ")
        elif i == 1:
            print("Por Proyecciones       ( {:10.4f}".format(Vector.x) + " ; " + "{:10.4f}".format(Vector.y) + " )")
        elif i == 2:
            print("Por Vectorial Polar    ( {:8.2f}".format(Vector.magnitud) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° )")
        elif i == 3:
            print("Por Vectorial Azimutal ( {:8.2f}".format(Vector.magnitud) + " ;< " + "{:11.4f}".format(Vector.DireccionAzimutal_g) + "° )")
        else:
            print("Ejemplo: VerVector(CVector) o VerVector(CVector, n) {n | n >= 0, n <= 3)")
    elif isinstance(Vector,CVector3D):
        if i is None:
            print("0). Por Vectores Unitarios             {:10.4f}".format(Vector.x) + " " + chr(238) + " + " + "{:10.4f}".format(Vector.y) + " " + chr(309) + " + " + "{:10.4f}".format(Vector.z) + " k\u0302")
            print("1). Por Proyecciones                   ( {:10.4f}".format(Vector.x) + " ; " + "{:10.4f}".format(Vector.y) + " ; " + "{:10.4f}".format(Vector.z) + " )")
            print("2). Por Vectorial Cilindricas Polar    ( {:8.2f}".format(Vector.magnitudxy) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° ; " + "{:10.4f}".format(Vector.z) + " )")
            print("3). Por Vectorial Cilindricas Azimutal ( {:8.2f}".format(Vector.magnitudxy) + " ;< " + "{:11.4f}".format(Vector.DireccionAzimutal_g) + "° ; " + "{:10.4f}".format(Vector.z) + " )")
            print("4). Por Vectorial Esfericas            ( {:8.2f}".format(Vector.magnitudxyz) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° ;< " + "{:10.4f}".format(Vector.DireccionZ_g) + "° )")
        elif i == 0:
            print("Por Vectores Unitarios             {:10.4f}".format(Vector.x) + " i\u0302 + " + "{:10.4f}".format(Vector.y) + " j\u0302 + " + "{:10.4f}".format(Vector.z) + " k\u0302 ")
        elif i == 1:
            print("Por Proyecciones                   ( {:10.4f}".format(Vector.x) + " ; " + "{:10.4f}".format(Vector.y) + " ; " + "{:10.4f}".format(Vector.z) + " )")
        elif i == 2:
            print("Por Vectorial Cilindricas Polar    ( {:8.2f}".format(Vector.magnitudxy) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° ; " + "{:10.4f}".format(Vector.z) + " )")
        elif i == 3:
            print("Por Vectorial Cilindricas Azimutal ( {:8.2f}".format(Vector.magnitudxy) + " ;< " + "{:11.4f}".format(Vector.DireccionAzimutal_g) + "° ; " + "{:10.4f}".format(Vector.z) + " )")
        elif i == 4:
            print("Por Vectorial Esfericas            ( {:8.2f}".format(Vector.magnitudxyz) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° ;< " + "{:10.4f}".format(Vector.DireccionZ_g) + "° )")
        else:
            print("Ejemplo: VerVector(CVector) o VerVector(CVector, n) {n | n >= 0, n <= 4)")
    else:
        print("Error en el argumento del vector.")
    
