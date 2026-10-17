sonlar = input().split()

for son in sonlar:
    son = int(son)

    if son % 2 == 0:
        print("juft sonlar",son)
    else:
        print("toq sonlar",son)

        