prompt = "C:\\Python_Grund2023\\"
mapp = input('Vilken mapp finns filen i?')
filnamn = input('Vad heter text filen?')
pathen = prompt+mapp+"\\"+filnamn
with open(pathen, 'r',  encoding='UTF-8') as f:
    for i in f:
        print (i)
