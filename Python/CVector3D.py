#***************************************************************
# Objecto para el manejo de vectores, donde los ángulos están en
# radianes.
#           Fecha: 30/09/2023
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************
import math

class CVector3D:

    def __init__(self, xi=None, yj=None, zk=None):
        if (xi is not None and yj is not None and zk is not None):
            self.x = xi
            self.y = yj
            self.z = zk
        else:
            self.x = 0
            self.y = 0
            self.z = 0

    def __add__(self, other):
        nvo = CVector3D()
        nvo.x = self.x + other.x
        nvo.y = self.y + other.y
        nvo.z = self.z + other.z
        return nvo

    def __isub__(self, other):
        nvo = CVector3D()
        nvo.x = self.x - other.x
        nvo.y = self.y - other.y
        nvo.z = self.z - other.z
        return nvo

    def Rec(self, x_i, y_j, z_k):
        self.x=x_i
        self.y=y_j
        self.z=z_k

    def Cilindricas(self, MagXY, AngPolar, z_k):
        AngRad = AngPolar * math.pi / 180.0
        self.x = MagXY * math.cos(AngRad)
        self.y = MagXY * math.sin(AngRad)
        self.z=z_k

    def Esfericas(self, MagXYZ, AngPolarXY_g, Ang_Vertical_g):
        AngRadXY = AngPolarXY_g * math.pi / 180.0
        AngRadZ = Ang_Vertical_g * math.pi / 180.0
        self.x = MagXYZ * math.sin(AngRadZ) * math.cos(AngRadXY)
        self.y = MagXYZ * math.sin(AngRadZ) * math.sin(AngRadXY)
        self.z = MagXYZ * math.cos(AngRadZ)

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
        return self.DireccionZ_r * 180.0 / math.pi


