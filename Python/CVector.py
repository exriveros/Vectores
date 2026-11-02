#***************************************************************
# Objecto para el manejo de vectores en 2 dimensiones, donde los 
# ángulos están en radianes. Se puede expresar en grados.
#           Fecha: 28/10/2026
#           Elaboró: Ernesto Riveros Ospina
#***************************************************************
import math

class CVector:
    
    def __init__(self, xi=None, yj=None):
        if (xi is not None and yj is not None):
            self.x = xi
            self.y = yj
        else:
            self.x = 0
            self.y = 0

    def __add__(self, other):
        nvo = CVector()
        nvo.x = self.x + other.x
        nvo.y = self.y + other.y
        return nvo

    def __sub__(self, other):
        nvo = CVector()
        nvo.x = self.x - other.x
        nvo.y = self.y - other.y
        return nvo

    def __eq__(self, other):
        nvo = CVector
        nvo.x = other.x
        nvo.y = other.y

    def __neg__(self):
        return CVector(-self.x,-self.y)
        
    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Funciones que inicializan el vector
    def Azi_g(self, Mag, Dir_g): #Inicializa con datos de magnitud y direccion Azimutal.
        Dir = Dir_g * math.pi / 180.0
        self.x = Mag * math.sin(Dir)
        self.y = Mag * math.cos(Dir)

    def Pol_g(self, Mag, Dir_g): #Inicializa con datos de magnitud y direccion Polar.
        Dir = Dir_g * math.pi / 180.0
        self.x=Mag*math.cos(Dir)
        self.y=Mag*math.sin(Dir)

    def Rec(self, x_i,y_j): #Inicializa con datos de proyecciones
        self.x=x_i
        self.y=y_j

    def Deflexion_Rad(self, VectSigue):
        R = 0
        if isinstance(VectSigue,CVector):
            PPto=self.ProdPuntoV(VectSigue)
            S=PPto / (self.magnitud * VectSigue.magnitud)
            if S>1.0:
                S=1.0
            elif S<-1.0:
                S=-1.0
            #R=math.acos(PPto / (self.magnitud * VectSigue.magnitud))
            R=math.acos(S)
        return round(R,18)

    def Deflexion_Grad(self, VectSigue):
        R = 0
        if isinstance(VectSigue,CVector):
            PPto=self.ProdPuntoV(VectSigue)
            S=PPto / (self.magnitud * VectSigue.magnitud)
            if S>1.0:
                S=1.0
            elif S<-1.0:
                S=-1.0
            #R=math.acos(PPto / (self.magnitud * VectSigue.magnitud))*180.0/3.14159265358979323846264
            R=math.acos(S)*180.0/3.14159265358979323846264
        return round(R,18)

    def ProdPuntoV(self, VectB):
        R = 0
        if isinstance(VectB,CVector):
            R=VectB.x*self.x+VectB.y*self.y
        return R

    def SentidoDeflex(self, VectB):
        R = 0
        PrdX = 0
        if isinstance(VectB,CVector):
            PrdX = self.x * VectB.y - self.y * VectB.x
            if PrdX == 0:
                R = 0
            else:
                R = PrdX/math.fabs(PrdX)
        return R


    @property
    def magnitud(self):
        return math.sqrt( math.pow(self.x,2.0) + math.pow(self.y,2.0))

    @property
    def DireccionPolar_r(self):
        #-----------------------------------------------------------------------
        # utiliza para el cálculo el arcTan(y/x) que tiene mayor precisión
        sgn = 0
        if self.y >= 0:
            sgn =  1
        else:
            sgn =  -1

        if(self.magnitud != 0):
            if self.x == 0:
                if self.y > 0:
                    return math.pi / 2.0
                else:
                    return 3 * math.pi / 2.0
            else:
                if self.x > 0:                    
                    return (1-sgn) * math.pi + math.atan(self.y / self.x)
                else:
                    return math.pi + math.atan(self.y / self.x)
        else:
            return 0

    @property
    def DireccionAzimutal_r(self):
        #-----------------------------------------------------------------------
        # utiliza para el cálculo el arcTan(y/x) que tiene mayor precisión
        sgn = 0
        if self.x >= 0:
            sgn =  1
        else:
            sgn =  -1

        if(self.magnitud != 0):
            if self.y == 0:
                if self.x > 0:
                    return math.pi / 2.0
                else:
                    return 3 * math.pi / 2.0
            else:
                if self.y > 0:                    
                    return (1-sgn) * math.pi + math.atan(self.x / self.y)
                else:
                    return math.pi + math.atan(self.x / self.y)
        else:
            return 0

    @property
    def DireccionPolar_g(self):
        return round( self.DireccionPolar_r * 180.0 / math.pi,13)

    @property
    def DireccionAzimutal_g(self):
        return round( self.DireccionAzimutal_r * 180.0 / math.pi,13)

    @property
    def CosenosDirectores(self):
        R=CVector()
        R.x=self.x/self.magnitud
        R.y=self.y/self.magnitud
        return R

        return nvo



