tal_l = input('Skriv ett antal heltal med mellanslag emellan dem: ')
tal_lista = tal_l.split(" ")
#print(tal_lista)

len_l = len(tal_lista)

empty_list = []

empty_list.append(tal_lista[0])

for i in range(1, len_l):

    if tal_lista[i] not in empty_list:

        empty_list.append(tal_lista[i])

print(empty_list)


