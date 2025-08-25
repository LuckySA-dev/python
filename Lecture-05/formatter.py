def format_strings(*str1:str) -> str:
    
    if len(str1) == 1:
        return str1[0].replace(" ","-").upper()
    
    return "".join(str1).upper()

def main():
    
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)
    
    result = format_strings("Python", "is", "fun")
    print(result)
    
    result = format_strings("Hello World!")
    print(result)
    
if __name__ == "__main__":
    main()