def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                break
        else:
            return True
        n += 1
        
def is_diabolic(n):
    return "666" in str(n)

def glue():
    a = 0
    for j in range(100001):
        if is_diabolic(j) and is_prime(j):
            print(j)
            a += 1
    print (f"takich liczb jest {a}")
print(glue())
