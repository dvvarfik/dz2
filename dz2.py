input_s = input('Введите слово: ')
def palindrom(s):
    return  s == s[::-1]
print(palindrom(input_s))


