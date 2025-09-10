def sum_calculator(*numbers):
    return sum(numbers)

def rectangle_square_calculator(a, b):
    return a * b

numbers_list = [1, 3, 6, 8, 25]
rectangle_sides = (5, 6)

numbers_sum = sum_calculator(numbers_list)
print(numbers_sum)

rectangle_square = rectangle_square_calculator(rectangle_sides)
print(rectangle_square)