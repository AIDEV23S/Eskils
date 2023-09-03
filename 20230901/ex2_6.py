import math

half_time = int(input('Halveringstid: '))
n_years = int(input('Antal år: '))

l = math.log(2)/half_time

n0 = 100

n = n0*math.exp(-l*n_years)

print('Efter ', n_years, 'år återstår ', n, '%')