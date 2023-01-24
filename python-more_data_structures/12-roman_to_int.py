#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_rom = dict(I=1, IV=4, V=5, IX=9, X=10, L=50, XC=90,
                    C=100, D=500, CM=900, M=1000)
    last_char = ''
    resultat = 0
    for i in roman_string:
        x = '{}{}'.format(last_char, i)
        if x in dict_rom and last_char in dict_rom:
            resultat += dict_rom[x]
            resultat -= dict_rom[last_char]
        elif i in dict_rom:
            resultat += dict_rom[i]
        last_char = i
    return resultat
