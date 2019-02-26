def fizzbuzz(a, b):

    list_length = len(a + b)

    if(list_length % 5 == 0 and list_length % 3 == 0):
        return "fizzbuzz"

    elif (list_length % 5 == 0):
        return "buzz"

    elif (list_length % 3 == 0):
        return "fizz"

    else:
        return list_length

a = ['a','b','c',3,7]
b = ['d','e',5,8]
print(fizzbuzz(a, b))