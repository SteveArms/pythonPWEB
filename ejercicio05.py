#Importar
from chessPictures import *
from interpreter import draw

casillero = square.join(square.negative())
draw(casillero.horizontalRepeat(4).negative())