#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        result = ""
        if(i % 3 == 0):
            result += "Fizz"
        if(i % 5 == 0):
            result += "Buzz"
        print(result or str(i), end='')
        if(i is not 100):
            print(", ", end='')
