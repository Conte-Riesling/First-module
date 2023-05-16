# Function receives an array of strings.
#     Please return number of strings, which
#     length is at least 2 symbols and first character
#     is equal to the last character
##
#     Функция получает на вход массив строк. Вернуть надо количество строк,
#     которые не короче двух символов и у которых первый и последний
#     символ совпадают.

def compare_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count +=1
            return count