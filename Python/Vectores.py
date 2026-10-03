#***************************************************************
# Aplicacion Vectores
#           Fecha: 30/09/2026
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************

#----------------------------------------------------------------
# Carga las librerias OOP de vectores 2D y 3D
from CVector import CVector
from CVector3D import CVector3D

def SumeOp(ax, ay, bx, by):
    VectA = CVector()
    VectB = CVector()
    VectorR = CVector()
    
    VectA.x = ax
    VectA.y = ay
    
    VectB.x = bx
    VectB.y = by

    VectorR = VectA + VectB
    
    print("Por Proyecciones       ( {:10.4f}".format(VectorR.x) + " ; " + "{:10.4f}".format(VectorR.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionAzimutal_g) + "° )")

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
def RecAngPol(mag, DirPol_g):
    Vector = CVector()            # define la variable como vector 2D
    Vector.Pol_g(mag,DirPol_g)    # inicializa el vector con informacion vectorial polar
    print("( {:11.4f}".format(Vector.x) + "; " + "{:11.4f}".format(Vector.y) + " )") # presenta los resultados

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def RecAzi(mag, DirAzi_g):
    Vector = CVector()          # define la variable como vector 2D
    Vector.Azi_g(mag,DirAzi_g)  # inicializa el vector con informacion vectorial azimutal
    print("( {:11.4f}".format(Vector.x) + " ;< " + "{:11.4f}".format(Vector.y) + " )") # presenta los resultados

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Suma(MagVecA, DirVecA, MagVecB, DirVecB):
    #----------------------------------------------------------------
    # define las variables como vectores 2D
    VectorA = CVector()
    VectorB = CVector()
    VectorR = CVector()

    #----------------------------------------------------------------
    # inicializa los vectores con informacion vectorial polar
    VectorA.Pol_g(MagVecA,DirVecA)
    VectorB.Pol_g(MagVecB,DirVecB)

    #----------------------------------------------------------------
    #suma de los dos vectores y alimentan al vector resultante R
    VectorR.x = VectorA.x+VectorB.x
    VectorR.y = VectorA.y+VectorB.y

    #----------------------------------------------------------------
    # presenta los resultados
    print("Por Proyecciones       ( {:10.4f}".format(VectorR.x) + " ; " + "{:10.4f}".format(VectorR.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionAzimutal_g) + "° )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Suma_v2(MagVecA, DirVecA, MagVecB, DirVecB):
    #----------------------------------------------------------------
    # define las variables como vectores 2D
    VectorA = CVector()
    VectorB = CVector()

    #----------------------------------------------------------------
    # inicializa los vectores con informacion vectorial polar
    VectorA.Pol_g(MagVecA,DirVecA)
    VectorB.Pol_g(MagVecB,DirVecB)

    #----------------------------------------------------------------
    # suma al vector A el vector B con el operador __sum__
    VectorA += VectorB

    #----------------------------------------------------------------
    # presenta los resultados
    print("Por Proyecciones       ( {:10.4f}".format(VectorA.x) + " ; " + "{:10.4f}".format(VectorA.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorA.magnitud) + " ;< " + "{:11.4f}".format(VectorA.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorA.magnitud) + " ;< " + "{:11.4f}".format(VectorA.DireccionAzimutal_g) + "° )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Resta(MagVecA, DirVecA, MagVecB, DirVecB):
    #----------------------------------------------------------------
    # define las variables como vectores 2D
    VectorA = CVector()
    VectorB = CVector()
    VectorR = CVector()

    #----------------------------------------------------------------
    # inicializa los vectores con informacion vectorial polar
    VectorA.Pol_g(MagVecA,DirVecA)
    VectorB.Pol_g(MagVecB,DirVecB)

    #----------------------------------------------------------------
    # le suma al vector A el vector B en la libreria CVector.py
    VectorR.x = VectorA.x - VectorB.x
    VectorR.y = VectorA.y - VectorB.y

    #----------------------------------------------------------------
    # presenta los resultados
    print("Por Proyecciones       ( {:10.4f}".format(VectorR.x) + " ; " + "{:10.4f}".format(VectorR.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionAzimutal_g) + "° )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Resta_v2(MagVecA, DirVecA, MagVecB, DirVecB):
    #----------------------------------------------------------------
    # define las variables como vectores 2D
    VectorA = CVector()
    VectorB = CVector()

    #----------------------------------------------------------------
    # inicializa los vectores con informacion vectorial polar
    VectorA.Pol_g(MagVecA,DirVecA)
    VectorB.Pol_g(MagVecB,DirVecB)

    #----------------------------------------------------------------
    # le suma al vector A el vector B en la libreria CVector.py
    VectorA.Reste_Vect(VectorB)

    #----------------------------------------------------------------
    # presenta los resultados
    print("Por Proyecciones       ( {:10.4f}".format(VectorA.x) + " ; " + "{:10.4f}".format(VectorA.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorA.magnitud) + " ;< " + "{:11.4f}".format(VectorA.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorA.magnitud) + " ;< " + "{:11.4f}".format(VectorA.DireccionAzimutal_g) + "° )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def MulEsc(ValEscalar, MagVecA, DirVecA):
    VectorA = CVector()
    VectorR = CVector()

    #----------------------------------------------------------------
    # inicializa los vectores con informacion vectorial polar
    VectorA.Pol_g(MagVecA,DirVecA)

    #----------------------------------------------------------------
    # multiplica un valor escalar por el vector
    VectorR.x = ValEscalar * VectorA.x
    VectorR.y = ValEscalar * VectorA.y

    #----------------------------------------------------------------
    # presenta los resultados
    print("Por Proyecciones       ( {:10.4f}".format(VectorR.x) + " ; " +"{:10.4f}".format(VectorR.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionAzimutal_g) + "° )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def MulEsc_v(ValEscalar, Vector2D):
    #----------------------------------------------------------------
    # define el vector R y lo inicializa multiplicando por el escalar 
    R = CVector(ValEscalar * Vector2D.x, ValEscalar * Vector2D.y)
    
    return R

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def DivEsc_v(ValEscalar, Vector2D):
    #----------------------------------------------------------------
    # define el vector R y lo inicializa multiplicando por el escalar 
    R = CVector(Vector2D.x / ValEscalar, Vector2D.y / ValEscalar)
    
    return R
    
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def VerVector(Vector2D, i=None): #imprime el vector usando diferentes referencias
    if i is None:
        print("0). Por Vectores Unitarios   {:10.4f}".format(Vector2D.x) + " i + " + "{:10.4f}".format(Vector2D.y) + " j ")
        print("1). Por Proyecciones       ( {:10.4f}".format(Vector2D.x) + " ; " + "{:10.4f}".format(Vector2D.y) + " )")
        print("2). Por Vectorial Polar    ( {:8.2f}".format(Vector2D.magnitud) + " ;< " + "{:11.4f}".format(Vector2D.DireccionPolar_g) + "° )")
        print("3). Por Vectorial Azimutal ( {:8.2f}".format(Vector2D.magnitud) + " ;< " + "{:11.4f}".format(Vector2D.DireccionAzimutal_g) + "° )")
    elif i == 0:
        print("Por Vectores Unitarios   {:10.4f}".format(Vector2D.x) + " i + " + "{:10.4f}".format(Vector2D.y) + " j ")
    elif i == 1:
        print("Por Proyecciones       ( {:10.4f}".format(Vector2D.x) + " ; " + "{:10.4f}".format(Vector2D.y) + " )")
    elif i == 2:
        print("Por Vectorial Polar    ( {:8.2f}".format(Vector2D.magnitud) + " ;< " + "{:11.4f}".format(Vector2D.DireccionPolar_g) + "° )")
    elif i == 3:
        print("Por Vectorial Azimutal ( {:8.2f}".format(Vector2D.magnitud) + " ;< " + "{:11.4f}".format(Vector2D.DireccionAzimutal_g) + "° )")
    else:
        print("Ejemplo: VerVector(CVector) o VerVector(CVector, n) {n | n >= 0, n <= 3)")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdPunto2D(VectorA_2D, VectorB_2D):
    A=VectorA_2D
    B=VectorB_2D

    #----------------------------------------------------------------
    # calcula el producto punto de los vectores, con resultado escalar 
    R = (A.x * B.x) + (A.y * B.y)

    return R

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdPunto3D(VectorA_3D,VectorB_3D):
    A=VectorA_3D
    B=VectorB_3D
    
    #----------------------------------------------------------------
    # calcula el producto punto de los vectores, con resultado escalar 
    R = (A.x * B.x) + (A.y * B.y) + (A.z * B.z) 

    return R

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdCruz3D(VectorA_3D,VectorB_3D):
    A=VectorA_3D
    B=VectorB_3D
    R=CVector3D()
    #----------------------------------------------------------------
    # calcula el producto cruz de los vectores, con resultado vector 
    x = (+1) * (A.y * B.z - A.z * B.y)
    y = (-1) * (A.x * B.z - A.z * B.x)
    z = (+1) * (A.x * B.y - A.y * B.x)

    return R
    
    
