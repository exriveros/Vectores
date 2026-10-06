# Vectores con OOP utilizando Python
Para tener las funciones disponibles, debe copiar como mínimo CVector.py, Vectores3D.py y Vectores.py.

## El archivo <code style="color : blue"><ins>**Vectores.py**</ins></code> tiene las siguientes funciones de:
- ### Presentación
  * Polar(x,y) imprime el resultado un vector polar con magnitud y dirección usando las proyecciones.
  * Azimutal(x,y) imprime el resultado un vector azimutal con magnitud y dirección usando las proyecciones.
  * Rectangular(Mag,DirPol_g) Imprime el resultado de las proyecciones de un vector donde DirPol_g es el ángulo polar dado en grados con decimales.
  * Rectangular_Azi(Mag,DirAzi_g) Imprime el resultado de las proyecciones de un vector donde DirPol_g es el ángulo azimutal dado en grados con decimales.
  * VerVector(Vector, opcional presentación entero)
- ### Operacionales: 
  * MulEsc(ValEscalar, Mag_A, DirPol_g_A) Regresa el vector resultante.
  * DivEsc(ValEscalar, Mag_A, DirPol_g_A) Regresa el vector resultante.
  * ProdPunto(Vector_A, Vector_B) Regresa la magnitud resultante.
  * ProdCruz(Vector_A, Vector_B) Regresa el vector resultante.
  * A + B o A + B + C: Suma Vectores y regresa el vector resultante.
  * A - B o A - B - C: Resta Vectores y regresa el vector resultante.
>[!NOTE]
>Para crear un vector con proyecciones <code style="color : blue">a = CVector(3,4)</code>. Con Magnitud y Dirección en grados polar <code style="color: bue">r = CVector(); r.Pol_g(5,53.13010235)</code>.
>
>Se escriben en la línea de comandos. Ejemplo: <code style="color : blue">r = c - (a + MulEsc(3,b))</code> Operación de: restarle a C, la suma del vector A y
>tres veces el vector B. Para ver el vector resultante r <code style="color : blue">VerVector(r) o VerVector(r,0)</code>
el vector A y 3 veces el vector B.

## En el archivo <code style="color : blue">CVector.py</code> se define la clase, funciones y propiedades:
- ### Funciones Clase CVector():
  * \+
  * \-
  * =
  * +=
  * -=
  * Azi_g(Mag, Dir_g) Inicializa el vector con dirección Azimutal con ángulo en grados.
  * Pol_g(Mag, Dir_g) Inicializa el vector con dirección Polar con ángulo grados.
  * Rec(x_i,y_j) Inicializa el vector con coordenadas o proyecciones. También CVector(x, y).
- ### Propiedades:
  * magnitud
  * DireccionPolar_r      ... resultado en radianes
  * DireccionAzimutal_r   ... resultado en radianes
  * DireccionPolar_g      ... resultado en grados
  * DireccionAzimutal_g   ... resultado en grados
  * CosenosDirectores     ... resultado CVector()
- ### Funciones Clase CVector3D():
  * \+
  * \-
  * =
  * +=
  * -=
  * Cilindricas(Mag, DirPolar_g, z) Inicializa el vector con dirección Polar con ángulo en grados y elevación.
  * Esfericas(Mag, DirPolar_g, AngVertical_g) Inicializa el vector con dirección Polar con ángulo grados y ángulo vertical.
  * Rec(x, y, z) Inicializa el vecor con las proyecciones. También CVector3D(x, y, z).
- ### Propiedades:
  * magnitudxy
  * magnitudxyz
  * DireccionPolar_r      ... resultado en radianes
  * DireccionAzimutal_r   ... resultado en radianes
  * DireccionZ_r          ... resultado en radianes
  * DireccionPolar_g      ... resultado en grados
  * DireccionAzimutal_g   ... resultado en grados
  * DireccionZ_g          ... resultado en grados
  * CosenosDirectores     ... resultado CVector3D()
