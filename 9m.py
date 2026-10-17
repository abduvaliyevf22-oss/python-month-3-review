sozlar = input().split()

caunt={}

for soz in sozlar:
    if soz in caunt:
        caunt[soz] +=1
    else:
        caunt[soz] = 1

print(caunt)

