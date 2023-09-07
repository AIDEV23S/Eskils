tal = int(input('Ange ett heltal: '))

if tal < 0:
    exit()

tal_min = tal
tal_max = tal

while True:
    tal = int(input('Ange ett heltal: '))
    if tal < 0:
        break
    if tal < tal_min:
        tal_min = tal
    if tal > tal_max:
        tal_max = tal


print('min: ', tal_min)
print('max: ', tal_max)