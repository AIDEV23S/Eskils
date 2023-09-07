minuter = int(input('Hur många minuter ringer du per månad? '))
if minuter < 33:
    abonnemang = "Kontant"
if minuter > 66:
    abonnemang = "Plus"
else:
    abonnemang = "Normal"

print("Du bör välja abonnemanget: ", abonnemang)