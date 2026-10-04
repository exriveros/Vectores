#***************************************************************
# Aplicacion Vectores
#           Fecha: 30/09/2026
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************

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
        R = CVector3D(ValEscalar * Vector.x, ValEscalar * Vector.y, ValEscalar * Vector.z)
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
        R = CVector3D(Vector.x / ValEscalar, Vector.y / ValEscalar, Vector.z / ValEscalar)
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

        return R
    else:
        return 0

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def ProdCruz(VectorA,VectorB):
    if (isinstance(VectorA,CVector3D) and isinstance(VectorB,CVector3D)):
        A=VectorA
        B=VectorB
        R=CVector3D()
        #----------------------------------------------------------------
        # calcula el producto cruz de los vectores, con resultado vector 
        R.x = (+1) * (A.y * B.z - A.z * B.y)
        R.y = (-1) * (A.x * B.z - A.z * B.x)
        R.z = (+1) * (A.x * B.y - A.y * B.x)
    elif (isinstance(VectorA,CVector) and isinstance(VectorB,CVector)):
        R.x = 0
        R.y = 0
        R.z = (+1) * (A.x * B.y - A.y * B.x)
    else:
        R.x = 0
        R.y = 0
        R.z = 0        

    return R
    

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
            print("0). Por Vectores Unitarios   {:10.4f}".format(Vector.x) + " i + " + "{:10.4f}".format(Vector.y) + " j ")
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
            print("0). Por Vectores Unitarios             {:10.4f}".format(Vector.x) + " i + " + "{:10.4f}".format(Vector.y) + " j + " + "{:10.4f}".format(Vector.z) + " k ")
            print("1). Por Proyecciones                   ( {:10.4f}".format(Vector.x) + " ; " + "{:10.4f}".format(Vector.y) + " ; " + "{:10.4f}".format(Vector.z) + " )")
            print("2). Por Vectorial Cilindricas Polar    ( {:8.2f}".format(Vector.magnitudxy) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° ; " + "{:10.4f}".format(Vector.z) + " )")
            print("3). Por Vectorial Cilindricas Azimutal ( {:8.2f}".format(Vector.magnitudxy) + " ;< " + "{:11.4f}".format(Vector.DireccionAzimutal_g) + "° ; " + "{:10.4f}".format(Vector.z) + " )")
            print("4). Por Vectorial Esfericas            ( {:8.2f}".format(Vector.magnitudxyz) + " ;< " + "{:11.4f}".format(Vector.DireccionPolar_g) + "° ;< " + "{:10.4f}".format(Vector.DireccionZ_g) + "° )")
        elif i == 0:
            print("Por Vectores Unitarios             {:10.4f}".format(Vector.x) + " i + " + "{:10.4f}".format(Vector.y) + " j + " + "{:10.4f}".format(Vector.z) + " k ")
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
    
