pnr = input('personnummer: ')

siffra = int(pnr[-2])

if siffra%2 == 0:

    print('Kvinna')

else:
    print('Man')
