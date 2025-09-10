def amount_of_symbol_in_string(string):
    symbol_count = {}
    for symbol in string:
        if symbol in symbol_count:
             symbol_count[symbol] += 1
        elif symbol not in symbol_count:
             symbol_count[symbol] = 1
    print(symbol_count)

print(amount_of_symbol_in_string("abac"))
