def cammel_kebab_string(input):
    list_of_letters = list(input)
    for index in range(len(list_of_letters)):
            if index % 2 == 0:
                list_of_letters[index] = str(list_of_letters[index]).upper()
            else:
                list_of_letters[index]  = str(list_of_letters[index]).lower()

    
    return (''.join(list_of_letters)).replace(" ","-")

print(cammel_kebab_string("Моя о стрінга")=="МоЯ-О-СтРіНгА")
print(cammel_kebab_string("Моя о стрінга"))