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

    def __neg__(self):
        return CVector3D(-self.x,-self.y,-self.z)

    def __sub__(self, other):
        nvo = CVector3D()
        nvo.x = self.x - other.x
        nvo.y = self.y - other.y
        nvo.z = self.z - other.z
        return nvo

    def __eq__(self, other):
        nvo = CVector3D()
        nvo.x = other.x
        nvo.y = other.y
        nvo.z = other.z
        return nvo

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

    def Rec(self, x_i, y_j, z_k):
        self.x=x_i
        self.y=y_j
        self.z=z_k

    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Funciones que inicializan el vector
    def ProdPuntoVXY(self, VectSigue):
        R = 0
        if isinstance(VectSigue,CVector3D):
            R=VectSigue.x * Self.x + VectSigue.y * Self.y
        return R

    def ProdPuntoVXYZ(self, VectSigue):
        R = 0
        if isinstance(VectSigue,CVector3D):
            R=VectSigue.x * Self.x + VectSigue.y * Self.y + VectSigue.z * Self.z
        return R
                
    def Deflexion_RadXY(self, VectSigue):
        R = 0
        if isinstance(VectSigue,CVector3D):
            PPto=self.ProdPuntoVXY(VectSigue)
            S=PPto / (self.magnitud * VectSigue.magnitud)
            if S>1.0:
                S=1.0
            elif S<-1.0:
                S=-1.0
            #R=math.acos(PPto / (self.magnitud * VectSigue.magnitud))
            R=math.acos(S)
        return round(R,18)

                
    def Deflexion_RadXYZ(self, VectSigue):
        R = 0
        if isinstance(VectSigue,CVector3D):
            PPto=self.ProdPuntoVXYZ(VectSigue)
            S=PPto / (self.magnitud * VectSigue.magnitud)
            if S>1.0:
                S=1.0
            elif S<-1.0:
                S=-1.0
            #R=math.acos(PPto / (self.magnitud * VectSigue.magnitud))
            R=math.acos(S)
        return round(R,18)


    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Propiedades de los vectores 3D
    @property
    def magnitudxyz(self):
        return math.sqrt( math.pow(self.x,2.0) + math.pow(self.y,2.0) + math.pow(self.z,2.0))

    @property
    def magnitudxy(self):
        return math.sqrt( math.pow(self.x,2.0) + math.pow(self.y,2.0))

    @property
    def DireccionPolar_r(self):
        if self.magnitudxy != 0:
            if self.y >= 0:
                return math.acos(self.x/self.magnitudxy)
            else:
                return 2*math.pi - math.acos(self.x/self.magnitudxy)
        else:
            return 0
        
    @property
    def DireccionAzimutal_r(self):
        if self.magnitudxy != 0:
            if(self.x>=0):
                return math.acos(self.y/self.magnitudxy)
            else:
                return 2*math.pi - math.acos(self.y/self.magnitudxy)
        else:
            return 0
    
    @property
    def DireccionZ_r(self):
        if(self.magnitudxyz != 0):
            return math.acos(self.z / self.magnitudxyz)
        else:
            return 0

    @property
    def DireccionPolar_g(self):
        return self.DireccionPolar_r * 180.0 / math.pi

    @property
    def DireccionAzimutal_g(self):
        return self.DireccionAzimutal_r * 180.0 / math.pi

    @property
    def DireccionZ_g(self):
        return self.DireccionZ_r * 180.0 / math.pi

    @property
    def CosenosDirectores(self):
        R=CVector3D()
        if  self.magnitudxyz != 0:
            R.x = self.x / self.magnitudxyz
            R.y = self.y / self.magnitudxyz
            R.z = self.z / self.magnitudxyz
        else:
            R.x = 0
            R.y = 0
            R.z = 0
        return R


