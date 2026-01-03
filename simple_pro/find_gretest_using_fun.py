def my_function(*number):
    greatest = number[0]
    for num in number:
        if num > greatest:
            greatest = num
    return greatest
print(my_function(10, 20, 5, 40, 30))