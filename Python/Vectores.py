#***************************************************************
# Aplicacion Vectores
#           Fecha: 30/09/2026
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************
from CVector import CVector
from CVector3D import CVector3D

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Pol(x, y):
    Vector = CVector()

    #----------------------------------------------------------------
    # inicializa el vector con informacion vectorial polar
    Vector.Rec(x,y)

    #----------------------------------------------------------------
    # presenta los resultados
    print("( {:8.2f}".format(Vector.magnitud) + " ;< " + "{:8.4f}".format(Vector.DireccionPolar_g) + "° )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def RecPol(mag, DirPol_g):
    Vector = CVector()

    #----------------------------------------------------------------
    # inicializa el vector con informacion vectorial polar
    Vector.Pol_g(mag,DirPol_g)

    #----------------------------------------------------------------
    # presenta los resultados
    print("( {:11.4f}".format(Vector.x) + " ;< " + "{:11.4f}".format(Vector.y) + " )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def RecAzi(mag, DirAzi_g):
    Vector = CVector()

    #----------------------------------------------------------------
    # inicializa el vector con informacion vectorial azimutal
    Vector.Azi_g(mag,DirAzi_g)

    #----------------------------------------------------------------
    # presenta los resultados
    print("( {:11.4f}".format(Vector.x) + " ;< " + "{:11.4f}".format(Vector.y) + " )")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def Suma(MagVecA, DirVecA,MagVecB, DirVecB):
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
    
    
