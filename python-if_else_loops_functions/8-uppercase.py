#!/usr/bin/python3
def uppercase(str):
    for i in str:
        int_c = ord(i)
        if int_c >= 97 and int_c <= 122:
            int_c = int_c - 32
        print(f'{int_c:c}', end="")
    print()
