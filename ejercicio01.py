#Importar
from chessPictures import *
from interpreter import draw
fila = knight.join(knight.negative())
fila2 = fila.negative()
draw(fila2.up(fila))
