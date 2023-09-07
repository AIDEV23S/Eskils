konsonanter = 'bdfghjklmnpqrstvxz'

s1 = input('Skriv något? ')
s1 = s1.lower()
s2 = ""

for i in s1:
    s2 = s2 + i
    if i in konsonanter:
        s2 = s2 + "o" + i

print('\n___Rövarspråk___\n',s2)

n = len(s2)
m = 0

s4 = ""
s3 = s2+" "

for i in range(n):

    if m < n-2:

        if s3[m] in konsonanter and s3[m+1] == "o":
            if s3[m+2] == s3[m]:
                s4 = s4 + s3[m] 
                m = m+3

        if s3[m] in konsonanter and s3[m+1] == "o":
            if s3[m+2] != s3[m]:
                s4 = s4 + "o"
                m = m+1

        else:
            s4 = s4 + s3[m]
            m = m+1  

print('\n______Översättning_______\n', s4)

with open('rovarsprak.txt', 'w',  encoding='UTF-8') as sav:
    sav.write(s2)
