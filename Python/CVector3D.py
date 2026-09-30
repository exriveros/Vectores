#***************************************************************
# Objecto para el manejo de vectores, donde los ángulos están en
# radianes.
#           Fecha: 30/09/2023
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************
import math

class CVector3D:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def IniVec3D(self, xi, yj,zk):
        self.x=xi
        self.y=yj
        self.z=zk

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

    @property
    def magnitud(self):
        return math.sqrt( math.pow(self.x,2.0) + math.pow(self.y,2.0) + math.pow(self.z,2.0))

    @property
    def magnitudxy(self):
        return math.sqrt( math.pow(self.x,2.0) + math.pow(self.y,2.0))

    @property
    def DireccionPolar_r(self):
        if self.y>=0:
            return math.acos(self.x/self.magnitudxy)
        else:
            return 2*math.pi - math.acos(self.x/self.magnitud)

    @property
    def DireccionAzimutal_r(self):
        if(self.x>=0):
            return math.acos(self.y/self.magnitudxy)
        else:
            return 2*math.pi - math.acos(self.y/self.magnitud)
    @property
    def DireccionZ_r(self):
        return math.acos(self.z/self.magnitud)

    @property
    def DireccionPolar_g(self):
        return self.DireccionPolar_r * 180.0 / math.pi

    @property
    def DireccionAzimutal_g(self):
        return self.DireccionAzimutal_r * 180.0 / math.pi

    @property
    def DireccionZ_g(self):
        return self.DireccionAzimutal_r * 180.0 / math.pi


