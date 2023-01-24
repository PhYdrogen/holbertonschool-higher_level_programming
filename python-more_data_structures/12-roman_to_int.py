#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_rom = dict(I=1, IV=4, V=5, IX=9, X=10, L=50, XC=90,
                    C=100, D=500, CM=900, M=1000)
    resultat = 0
    char = ''
    spec = ''
    j = 0
    for i in range(len(roman_string)):
        if j >= len(roman_string):
            break
        char = roman_string[j]
        if roman_string[j] == 'I' and j + 1 < len(roman_string):
            spec = '{}{}'.format(char, roman_string[j+1])
            if spec in dict_rom:
                resultat += dict_rom[spec]
                j += 2
                continue
        else:
            resultat += dict_rom[char]
            j += 1
    return resultat
