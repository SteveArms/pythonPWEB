#Importar
from chessPictures import *
from interpreter import draw
arriba = knight.join(knight.negative())
abajo = arriba.verticalMirror()
draw(abajo.up(arriba))