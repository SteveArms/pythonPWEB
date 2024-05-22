#Importar
from chessPictures import *
from interpreter import draw

casilleroX2 = square.negative().join(square)
fila = casilleroX2.horizontalRepeat(4)
fila = fila.up(fila.negative())
draw(fila.verticalRepeat(2))