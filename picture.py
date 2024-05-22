from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:      
      return color
    return inverter[color]
  
  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
        vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    nuevo = []
    for i in range(len(self.img) - 1 , -1, -1):
      nuevo.append(self.img[i])
    return Picture(nuevo)

  def negative(self):
    nuevo = []
    for i in range(len(self.img)):
      cadenaFinal = ""
      cadena = self.img[i]
      for x in range(len(cadena)):
        cadenaFinal += self._invColor(cadena[x])
      nuevo.append(cadenaFinal) 
    return Picture(nuevo)

  def join(self, p):
    nuevo = []
    for i in range(len(self.img)):
      nuevo.append(self.img[i] + p.img[i])
    return Picture(nuevo)

  def up(self, p):
    nuevo = []
    for i in range(len(self.img) + len(p.img)):
      if i < 58:
        nuevo.append(p.img[i])
      else:
        nuevo.append(self.img[i % 58])
    return Picture(nuevo)

  def under(self, p):
    nuevo = []
    for i in range(len(p.img)):
      cadenaFinal = ""
      cadena = p.img[i]
      for x in range(len(cadena)):
        if(cadena[x] == ' '):
          cadenaAuxiliar = self.img[i]
          cadenaFinal += cadenaAuxiliar[x]
        else :
          cadenaFinal += cadena[x]
      nuevo.append(cadenaFinal)
    return Picture(nuevo)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    nuevo = []
    for i in range(len(self.img)):
      cadena = ""
      for y in range(n):
        cadena += self.img[i]
      nuevo.append(cadena)
    return Picture(nuevo)

  def verticalRepeat(self, n):
    nuevo = []
    for i in range(n):
      for y in range(len(self.img)):
        nuevo.append(self.img[y])
    return Picture(nuevo)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    nuevo = []
    for i in range(len(self.img[0]) - 1, -1 ,-1):
      cadenaNueva = ""
      for x in range(len(self.img)):
        cadenaNueva += self.img[x][i]
      nuevo.append(cadenaNueva)
    return Picture(nuevo)