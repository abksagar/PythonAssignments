from sys import getsizeof
inputNumber= int(input("Enter a number: "))

print("Data Type of inputNumber is: ", type(inputNumber))
print("Memory address of inputNumber is: ", id(inputNumber))
#print("Size of inputNumber in bytes is: ", inputNumber.__sizeof__())
print("Size of inputNumber in bytes using getsizeof() is: ", getsizeof(inputNumber))