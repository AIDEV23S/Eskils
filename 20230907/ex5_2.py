import datetime

pnr = input('Ange ditt personnummer 10 tecken utan bindestreck: ')

fÅr = pnr[0:2]
fMån = pnr[2:4]
fDag = pnr[4:6]

dt = datetime.datetime.now()
dDatum =str(dt.date())

#print(dDatum, pnr)

dMån = dDatum[dDatum.find('-')+1:dDatum.find('-')+3]
dDag = dDatum[dDatum.rfind('-')+1:dDatum.rfind('-')+3]

#print(dMån, dDag, fMån, fDag)

if dMån == fMån and dDag == fDag:
    print('Grattis på födelsedagen!')
else:
    print('Du fyller inte år idag!')