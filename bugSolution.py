def my_function(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

#The bug is that the function does not handle the case where a and b are equal. This can lead to unexpected behavior.
result = my_function(5,5)
print(result) # Output:5