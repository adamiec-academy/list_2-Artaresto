def multiplication_table(x1, x2, y1, y2):
    lenght = len(str(x2*y2)) + 1
    c = x1
    d = x2
    a = " " * lenght + "|"
    b = " "
    second = 0
    for first in range(c,d + 1):
        if first == x1:
            print(a, end=b*(lenght -1))
        else:
            c += 1
            second += 1
            if c == x2:
                print(c, end="")
                break
        print(f"{c}{b * (lenght - 1)}", end="")


    print("",end="\n")
    if x2*y2 > 100:
        second -= 1
    print("-" * ((second + 1)+ lenght + x2 * (lenght - 1) - lenght))
    
    for collumn in range(y1, y2+1):
        a = len(str(collumn))
        free_space = lenght - a - 1
        outcome = " " * free_space + str(collumn) + " " + "|"
        for row in range(x1, x2+1):
            a = len(str(collumn * row))
            free_space = lenght - a 
            outcome += " " * free_space + str(collumn*row)
        print(outcome)

