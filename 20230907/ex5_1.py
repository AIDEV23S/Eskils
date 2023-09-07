s1 = input('Skriv en mening innehållande minst två ord och ett eller flera mellan slag:')

s1_l = len(s1)

print(f"Antal inmatade tecken: {s1_l}")


s1 = s1.strip()

print(s1)

n = 0
for i in s1:
    if i == " ":
        n +=1

print(f'antal mellanslag kvar {n}')
print(f"Antal möjliga ord {n+1}")

s2 = s1.split(" ")
s2_ord = len(s2)
print(s2_ord)

print('första ordet: ', s2[0])
print('sista ordet: ', s2[s2_ord-1])
      

