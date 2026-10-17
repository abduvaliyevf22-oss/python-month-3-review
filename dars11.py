sonlar = []

for son1 in range(5):
    son = int(input("Son kiriting: "))
    sonlar.append(son)

yigindi=sum(sonlar)
print("yigindisi",yigindi)
eng_katta = max(sonlar)
print("eng kattasi",eng_katta)
eng_kichik = min(sonlar)
print("eng kichigi",eng_kichik)
ortachasi = sum(sonlar) / len(sonlar)
print("ortachasi",ortachasi)