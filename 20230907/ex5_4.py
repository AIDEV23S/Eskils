konsonanter = 'bdfghjklmnpqrstvxz'

s1 = input('Skriv något? ')
s1 = s1.lower()
s2 = ""

for i in s1:
    s2 = s2 + i
    if i in konsonanter:
        s2 = s2 + "o" + i

print(s2)