def multiplication_table(x1, x2, y1, y2):
    lenght = len(str(x2*y2))
    a = " " * lenght + "|"
    b = " "
    second = 0
    for first in range(x1,x2 + 1):
        if first == x1:
            print(a, end=b*lenght)
        else: 
            x1 += 1
            second += 1
        print(f"{x1}{b * lenght }", end="")

    print(" ",end="\n")
    print("-" * (second+lenght+x2*lenght))  
    
    for collumn in range(y1, y2+1):
        a = len(str(collumn))
        free_space = lenght - a - 1
        outcome = " " * free_space + str(collumn) + " " + "|"

        for row in range(x1, x2+1):
            a = len(str(collumn * row))
            free_space = lenght - a + 1
            outcome += " " * free_space + str(collumn*row)
        print(outcome)

