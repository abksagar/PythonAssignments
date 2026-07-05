# lambda function using filter  which accept list of string and return string whos lenght greater than 5

GreaterThan5= lambda strings: list(filter(lambda string: len(string) > 5, strings))

def main():
    strings= list(map(str,input("Enter string ").split()))
    result= GreaterThan5(strings)
    print("String with length greater than 5 are:",result)


if __name__ == "__main__":
    main()    