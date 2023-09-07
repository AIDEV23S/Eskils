import math
a = float(input('sida a: '))
b = float(input('sida b: '))
alfa = float(input('vinkel alfa i grader: '))
alfa_rad = alfa*math.pi/180
c = math.sqrt(a**2+b**2-2*a*b*math.cos(alfa_rad))

if abs(a - b) < 1e-10 and abs(a - c) < 1e-10:
    print('Triangeln är liksidig')
if abs(a - b) < 1e-10 and abs(a - c) > 1e-10:
    print('Triangeln är likbent')
if abs(a-b) > 1e-10 and abs(a-c) > 1e-10:
    print('Triangeln är oliksidig')
