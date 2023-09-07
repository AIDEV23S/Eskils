konsonanter = 'bdfghjklmnpqrstvxz'

s1 = input('Skriv något på rövarspråk? ')
s2 = s1.lower()

n = len(s2)
m = 0
s3 = s2+" "
s4 = ""

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