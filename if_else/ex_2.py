oper1 = 2
while oper1 <= 12:
    print("[", oper1, "]")
    num1 = 1
    while num1 <= 12:
        print(oper1, "*", num1, ":", oper1 * num1, " ")
        num1 += 1
    print("")
    oper1 += 1
    print("---------------")

#######################################################

table = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for table in table:
    print("[", table, "]")
    for num in number:
        print(table, " * ", num, " : ", table * num)
    print("------------")
