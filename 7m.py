sonlar = list(map(int, input().split()))
sonlar = list(set(sonlar))
sonlar.sort()

print("Ikkinchi eng katta son:", sonlar[-2])