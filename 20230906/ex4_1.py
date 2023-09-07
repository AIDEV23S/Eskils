n = int(input('antal heltal att mata in: '))

tal_max = 0
tal_min = 0

m = n

while n !=0:

    tal = int(input('Tal: '))

    if tal <= 0:
        print('Otillåtet tal, Programmet avslutas')
        break

    if n == m:
        tal_min = tal

    if tal > tal_max:
        tal_max = tal

    if tal <= tal_min:
        tal_min = tal
        
    n -= 1

if tal_min > 0:
    print('\n___________\n'+f'min: {tal_min} max: {tal_max}'+'\n__________\n')
