def analyze_array(data):
    result = {}
    for number in data:
        number_string = str(number)
        unique_numbers = []
        sum_of_unique_numbers = 0
        
        for unique_num in number_string:
            if unique_num not in unique_numbers:
                unique_numbers.append(unique_num)
        result[number_string] = len(unique_numbers)
    return result

data = [123, 112, 405, 303, 99]  
print(analyze_array(data))