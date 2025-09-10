# def create_even_list(a):
#     even_list = []
#     for i in range(1, a):
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list

# print(create_even_list(20))

# def create_odd_list(a):
#     odd_list = []
#     for i in range(1, a):
#         if i % 2 != 0:
#             odd_list.append(i)
#     return odd_list

# print(create_odd_list(20))


# def create_even_list_more10(a):
#     even_list = []
#     for i in range(1, a):
#         if i % 2 == 0 and i > 10:
#             even_list.append(i)
#     return even_list

# print(create_even_list_more10(20))

def filter_number_condition(a, condition):
    result_list = []
    for i in range(0, a):
        if condition(i):
            result_list.append(i)
    return result_list

print(filter_number_condition(20, lambda i: i % 2 == 0))
print(filter_number_condition(20, lambda i: i % 2 != 0))
print(filter_number_condition(20, lambda i: i % 2 == 0 and i>10 and i <=18))
