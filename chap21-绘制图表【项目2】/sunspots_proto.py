# -*- coding: utf-8  -*-
# 太阳黑子图形程序的第一个原型(sunspots_proto.py)

from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
# Year Month  Predicted high Low
    (2019, 5,         69.2 ,   70.2,    68.2),
    (2019, 6 ,        68.7,    69.7 ,   67.7),
    (2019, 7,         68.0,    70.0,    66.0),
    (2019, 8 ,        67.2 ,   70.2 ,   64.2),
    (2019 ,9,66.5 ,70.5 ,   62.5),
    (    2019 ,10 ,        65.6 ,   69.6,    61.6),
    (2019 ,11  ,       64.7 ,   69.7 ,   60.0),
    (2019 ,12 ,        64.0 ,   70.0 ,   60.0),
    (2020 ,1 ,        63.5  ,  70.5 ,   60.0),
    (2020 ,2,         62.9 ,   70.9 ,   60.0),
    (2020 ,3 ,        62.4 ,   70.4 ,   60.0),
    (2020 ,4 ,        61.8 ,   70.8,    60.0),
    (2020 ,5 ,        61.4 ,   70.4,    60.0),
    (2020 ,6 ,        61.1 ,   70.1,    60.0),
    (2020 ,7 ,        60.9 ,   69.9 ,   60.0),
    (2020 ,8 ,        60.7 ,   69.7,    60.0),
    (2020,9 ,        60.6 ,   69.6,    60.0),
(2020 ,10   ,      60.4   , 69.4,    60.0)
]

drawing = Drawing(200, 150)
pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low = [row[4]-40 for row in data]
times = [200*((row[0] + row[1]/12.0) - 2019)-110 for row in data]
drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))

drawing.add(String(65, 115, 'Sunpots', fontSize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
