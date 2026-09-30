# Vectores con OOP utilizando Python
Para tener las funciones disponibles, debe copiar como mínimo CVector.py y Vectores.py.

En el archivo Vectores.py se tienen las funciones:
- Pol(x,y)
- RecPol(Mag,DirPol_g) donde DirPol_g es el ángulo polar dado en grados con decimales.
- RecAzi(Mag,DirAzi_g) donde DirAzi_g es el ángulo azimutal dado en grados con decimales.
- Suma(Mag_A, DirPol_g_A, Mag_B, DirPol_g_B)
- MulEsc(ValEscalar, Mag_A, DirPol_g_A)
- ProdPunto2D(Mag_A, DirPol_g_A, Mag_B, DirPol_g_B)
- ProdPunto3D(xa, ya, za, xb, yb, zb)
- ProdCruz3D(xa, ya, za, xb, yb, zb)
  
En el archivo CVector.py se define la clase, funciones y propiedades:
- Funciones:
* Pol_g(Mag, Dir_g)
* Azi_g(Mag, Dir_g)
* Rec(self, x_i,y_j)
- ## Propiedades:
  * magnitud
  * DireccionPolar_r      ... resultado en radianes
  * DireccionAzimutal_r   ... resultado en radianes
  * DireccionPolar_g      ... resultado en grados
  * DireccionAzimutal_g   ... resultado en grados
