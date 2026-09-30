# Vectores con OOP utilizando Python
Para tener las funciones disponibles, debe copiar como mínimo CVector.py, Vectores3D.py y Vectores.py.

El archivo <code style="color : blue"><ins>**Vectores.py**</ins></code> tiene las funciones:
- Pol(x,y) imprime el resultado un vector polar con magnitud y dirección usando las proyecciones.
- RecPol(Mag,DirPol_g) Imprime el resultado de las proyecciones de un vector donde DirPol_g es el ángulo polar dado en grados con decimales.
- RecAzi(Mag,DirAzi_g) Imprime el resultado de las proyecciones de un vector donde DirPol_g es el ángulo azimutal dado en grados con decimales.
- Suma(Mag_A, DirPol_g_A, Mag_B, DirPol_g_B) Imprime el resultado de la resta de los dos vectores.
- Suma_v2(Mag_A, DirPol_g_A, Mag_B, DirPol_g_B) Imprime el resultado de restar al VectorA el VectorB.
- Resta(MagVecA, DirVecA, MagVecB, DirVecB) Imprime el resultado de la resta de los dos vectores.
- Resta_v2(MagVecA, DirVecA, MagVecB, DirVecB) Imprime el resultado de restar al VectorA el VectorB.
- MulEsc(ValEscalar, Mag_A, DirPol_g_A) Imprime el resultado multiplicar un Valor Escalar al VectorA. No afecta el VectorA.
- MulEsc_v2(ValEscalar, Mag_A, DirPol_g_A) Imprime el resultado del VectorA al multiplicarlo por un Valor Escalar. Afecta al VectorA.
- ProdPunto2D(Mag_A, DirPol_g_A, Mag_B, DirPol_g_B)
- ProdPunto3D(xa, ya, za, xb, yb, zb)
- ProdCruz3D(xa, ya, za, xb, yb, zb)
  
## En el archivo <code style="color : blue">CVector.py</code> se define la clase, funciones y propiedades:
- ### Funciones:
  * Pol_g(Mag, Dir_g)
  * Azi_g(Mag, Dir_g)
  * Rec(x_i,y_j)
  * Sume_Vect(VectorB) Afecta el vector.
  * Reste_Vect(VectorB) Afecta el vector.
  * Mult_Escalar(ValEscalar) Afecta el vector.
- ### Propiedades:
  * magnitud
  * DireccionPolar_r      ... resultado en radianes
  * DireccionAzimutal_r   ... resultado en radianes
  * DireccionPolar_g      ... resultado en grados
  * DireccionAzimutal_g   ... resultado en grados
