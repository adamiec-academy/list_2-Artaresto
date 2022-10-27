def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if (n % i) == 0:
                return False
            else:
                return True
     
        
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
