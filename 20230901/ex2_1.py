mil_now = int(input('Mätarställning idag: '))
mil_then = int(input('Mätarställning ett år sedan: '))
mil_driven = mil_now - mil_then
liter_bensin = float(input('Antal liter bensin: '))
forbr_mil = liter_bensin/mil_driven
print('\n...........\n')
print('Mätarställning idag: ', mil_now)
print('Mätarställning 1 år sedan: ', mil_then)
print(f'Antal körda mil: {mil_driven}')
print(f'Förbrukning liter bensin: {liter_bensin}')
print(f'Förbrukning liter/mil: {forbr_mil:.3f}')