# Написати функцію яка буде приймати стрічку та букву, і рахувати кількість однакових заданих букв в реченні

def find_numbers_of_letters_in_sentence(input_string, target_char):
    list_of_letters = list(input_string)
    
    similar_letters_result = 0
    for char in list_of_letters:
        if char.lower() == target_char.lower():
            similar_letters_result += 1
    if similar_letters_result >= 1:
         print(f'Буква "{target_char}" повторяється в реченні "{similar_letters_result}" разів')
    else:
        print("Не знайдено")
    

sentence = input("Введіть речення: ")
letter = input("Введіть букву: ")

print(find_numbers_of_letters_in_sentence(sentence, letter))