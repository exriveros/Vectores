# Vectores con OOP utilizando Python
Para tener las funciones disponibles, debe copiar como mínimo CVector.py, Vectores3D.py y Vectores.py.

## El archivo <code style="color : blue"><ins>**Vectores.py**</ins></code> tiene las siguientes funciones:
- Polar(x,y) imprime el resultado un vector polar con magnitud y dirección usando las proyecciones.
- Azimutal(x,y) imprime el resultado un vector azimutal con magnitud y dirección usando las proyecciones.
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

>[!NOTE]
  Se escriben en la línea de comandos. Ejemplo: <code style="color : blue">Suma(4, 45, 8, 135)</code> Realiza la Suma del vector (4;< 45°) con el vector (8;< 135°).
## En el archivo <code style="color : blue">CVector.py</code> se define la clase, funciones y propiedades:
- ### Funciones:
  * \+
  * \-
  * =
  * Pol_g(Mag, Dir_g) Inicializa el vector con dirección Polar con ángulo grados.
  * Azi_g(Mag, Dir_g) Inicializa el vector con dirección Azimutal con ángulo en grados.
  * Rec(x_i,y_j) Inicializa el vector con coordenadas o proyecciones.
  * Sume_Vect(VectorB) Afecta el vector sumando el VectorB.
  * Reste_Vect(VectorB) Afecta el vector sumando el VectorB.
  * Mult_Escalar(ValEscalar) Afecta el vector multiplicándolo por el valor escalar.
- ### Propiedades:
  * magnitud
  * DireccionPolar_r      ... resultado en radianes
  * DireccionAzimutal_r   ... resultado en radianes
  * DireccionPolar_g      ... resultado en grados
  * DireccionAzimutal_g   ... resultado en grados
