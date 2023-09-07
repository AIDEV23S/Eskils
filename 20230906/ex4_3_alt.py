antal_dagar = 1
dagens_lön = 0.01
totalt_belopp = 0.01
while totalt_belopp < 10000000:
    antal_dagar = antal_dagar+1
    dagens_lön = dagens_lön*2
    totalt_belopp = totalt_belopp+dagens_lön

print('du måste jobba: ', antal_dagar, 'dagar')