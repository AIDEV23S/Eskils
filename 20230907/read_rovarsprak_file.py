konsonanter = 'bdfghjklmnpqrstvxz'

with open('rovarsprak.txt','r',encoding='UTF-8') as f:

    for s in f:

# författarens lösning

        i = 0
        while i < len(s):
            print(s[i], end ="")
            t = s[i].lower()
            if t in konsonanter:
                i +=3
            else:
                i +=1
                


