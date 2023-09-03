import math
x1, y1 = int(input('X1: ')),int(input('y1: '))
x2, y2 = int(input('X2: ')),int(input('y2: '))

xdiff = x1-x2
ydiff = y1-y2

s = math.sqrt(xdiff**2+ydiff**2)

print(f'avstånd: {s}')