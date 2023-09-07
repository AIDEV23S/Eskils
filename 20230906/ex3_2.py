import math
radie = float(input('Cirkelns radie: '))
if radie <= 0:
    print('Radien måste vara ett tal större än 0!')

else:

    omkrets = math.pi*2*radie
    area = math.pi*radie**2

    print(f'omkrets: {omkrets:.2f} area: {area:.2f}')

