def is_armstrong(n:int):
    str_n = str(n)
    power = len(str_n)
    total = [int(digit) ** power for digit in str_n]
    display = " + ".join(f"{digit}^{power}" for digit in str_n)
    return sum(total) == n, f"({n} = {display})"

def main():
    print(is_armstrong(153))
    print(is_armstrong(9474))
    print(is_armstrong(123))

if __name__ == "__main__":
    main()