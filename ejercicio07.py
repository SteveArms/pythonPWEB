#Importar
from chessPictures import *
from interpreter import draw

cTorre = square.negative().under(rock)
cCaballo = square.under(knight)
cAlfil = square.negative().under(bishop)
cReyna = square.under(queen)
cRey = square.negative().under(king)
cAfil2 = square.under(bishop)
cCaballo2 = square.negative().under(knight)
cTorre2 = square.under(rock)
cPeon = square.under(pawn).join(square.negative().under(pawn))
#Fila Peones
filaPeones = cPeon.horizontalRepeat(4)
#Fila Piezas
filaPiezas = cTorre.join(cCaballo).join(cAlfil).join(cReyna).join(cRey).join(cAfil2).join(cCaballo2).join(cTorre2)
#Fila medio
casillerox2 = square.negative().join(square)
fila = casillerox2.horizontalRepeat(4)
filax2 = fila.up(fila.negative())
tM = filax2.verticalRepeat(2)
#Tablero final
tablero = filaPiezas.up(filaPeones).up(tM).up(filaPeones.negative()).up(filaPiezas.negative())

draw(tablero)