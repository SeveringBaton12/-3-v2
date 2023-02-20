def roman_to_int(roman):
    roman_numerals = {'I': 1, 'II' : 2 ,'III' : 3 ,'IV' : 4 ,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(roman)):
        if i > 0 and roman_numerals[roman[i]] > roman_numerals[roman[i-1]]:
            int_val += roman_numerals[roman[i]] - 2 * roman_numerals[roman[i-1]]
        else:
            int_val += roman_numerals[roman[i]]
    return int_val

def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 3, 2, 1]
    syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'III','II','I']
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num