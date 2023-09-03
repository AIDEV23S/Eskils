#miles = int(input('miles: '))
#mil = float(miles*1.609)/10
#gallons = int(input('gallons; '))
#liter = float(gallons*3.785)

#mpg = miles/gallons
#lpm = liter/mil

#print('miles per gallon: ', mpg)
#print('liter per mil: ', lpm)

mpg = float(input('Miles/gallons: '))

mpg_inv = 1/mpg #gallons/mile

lpm_t = mpg_inv*3.785/(1.609/10) #liter per mil conversion

print(mpg, f'miles/gallons motsvarar {lpm_t:.3f} liter/mil')
