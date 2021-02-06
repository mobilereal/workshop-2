opre = 2
while opre <= 12:
    print("[", opre, "]")
    num = 1
    while num <= 12:
        print(opre, "*", num, ":", opre * num, " ")
        num += 1
    print("")
    opre += 1
    print("---------------------")