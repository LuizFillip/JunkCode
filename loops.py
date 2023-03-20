lenght = 19
for i in range(lenght):
    for j in range(lenght):
        if j % 2 == 0:
            if (j >= (abs(4 - i) * 2 - 1)):
                print(j + 2, end = "")
            else:
                print(" ", end = "")
        else:
            print(" ", end = "")
    print()