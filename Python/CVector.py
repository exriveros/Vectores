#***************************************************************
# Objecto para el manejo de vectores, donde los ángulos están en
# radianes.
#           Fecha: 30/09/2023
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************
import math

class CVector:

    def __init__(self):
        self.x = 0
        self.y = 0        

    def Pol_g(self, Mag, Dir_g):
        Dir = Dir_g * math.pi / 180.0
        self.x=Mag*math.cos(Dir)
        self.y=Mag*math.sin(Dir)

    def Azi_g(self, Mag, Dir_g):
        Dir = Dir_g * math.pi / 180.0
        self.x = Mag * math.sin(Dir)
        self.y = Mag * math.cos(Dir)

    def Rec(self, x_i,y_j):
        self.x=x_i
        self.y=y_j

    def Sume_Vect(self, VecB):
        self.x = self.x + VecB.x
        self.y = self.y + VecB.y

    def Reste_Vect(self, VecB):
        self.x = self.x - VecB.x
        self.y = self.y - VecB.y

    def Mult_Escalar(self, ValEscalar):
        self.x = ValEscalar * self.x
        self.y = ValEscalar * self.y

    @property
    def magnitud(self):
        return math.sqrt( math.pow(self.x,2.0) + math.pow(self.y,2.0))

    @property
    def DireccionPolar_r(self):
        if self.y>=0:
            return math.acos(self.x/self.magnitud)
        else:
            return 2*math.pi - math.acos(self.x/self.magnitud)

    @property
    def DireccionAzimutal_r(self):
        if(self.x>=0):
            return math.acos(self.y/self.magnitud)
        else:
            return 2*math.pi - math.acos(self.y/self.magnitud)

    @property
    def DireccionPolar_g(self):
        return self.DireccionPolar_r * 180.0 / math.pi

    @property
    def DireccionAzimutal_g(self):
        return self.DireccionAzimutal_r * 180.0 / math.pi

