# def generate_primes(end:int):
    
#     my_set = set()
#     if end < 2:
#         return "\"\""
    
#     for x in range(1, end):
#         if x % 2 != 0:
#             my_set.add(x)
            
#     return ", ".join(map(str, my_set))        
    
def generate_primes(n:int):
    
    if n < 2:
        return "\"\""
    
    prime = []
    for num in range(2, n + 1):
        if all(num % p != 0 for p in prime):
            prime.append(num
            )
    return ", ".join(map(str, prime))


def main():
    print(generate_primes(10))
    print(generate_primes(20))
    print(generate_primes(1))
    print(generate_primes(2))

if __name__ == "__main__":
    main()