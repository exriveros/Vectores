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
    print("Por Proyecciones       ( {:10.4f}".format(VectorR.x) + " ; " + "{:10.4f}".format(VectorR.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorR.magnitud) + " ;< " + "{:11.4f}".format(VectorR.DireccionAzimutal_g) + "° )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def MulEsc_v2(ValEscalar, MagVecA, DirVecA):
    VectorA = CVector()

    #----------------------------------------------------------------
    # inicializa los vectores con informacion vectorial polar
    VectorA.Pol_g(MagVecA,DirVecA)

    #----------------------------------------------------------------
    # multiplica un valor escalar por el vector
    VectorA.Mult_Escalar(ValEscalar)

    #----------------------------------------------------------------
    # presenta los resultados
    print("Por Proyecciones       ( {:10.4f}".format(VectorA.x) + " ; " + "{:10.4f}".format(VectorA.y) + " )")
    print("Por Vectorial Polar    ( {:8.2f}".format(VectorA.magnitud) + " ;< " + "{:11.4f}".format(VectorA.DireccionPolar_g) + "° )")
    print("Por Vectorial Azimutal ( {:8.2f}".format(VectorA.magnitud) + " ;< " + "{:11.4f}".format(VectorA.DireccionAzimutal_g) + "° )")


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdPunto2D(MagVecA, DirVecA,MagVecB, DirVecB):
    VectorA = CVector()
    VectorB = CVector()

    #----------------------------------------------------------------
    # inicializa los vectores con informacion vectorial polar
    VectorA.Pol_g(MagVecA,DirVecA)
    VectorB.Pol_g(MagVecB,DirVecB)

    R = VectorA.x*VectorB.x + VectorA.y*VectorB.y

    print("Prod Punto 2D{:8.2f}".format(R))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdPunto3D(xa, ya, za, xb, yb, zb):

    R = (xa * xb) + (ya * yb) + (za * zb)

    print("Prod Punto 3D{:8.2f}".format(R))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdCruz3D(xa, ya, za, xb, yb, zb):

    x = (+1) * (ya * zb - yb * za)
    y = (-1) * (xa * zb - xb * za)
    z = (+1) * (xa * yb - xb * ya)

    print("Prod Cruz 3D{:8.2f}".format(x) + "i + {:8.2f}".format(y) + "j + {:8.2f}".format(z) + "k")
    
    
