#     Function receives a long string with many words.
#     It should return the same string, but words,
#     larger then 6 symbols should be changed, symbols
#     after the sixth one should be replaced by symbol *
#     :param string
#     :returns string
#
#      Функция получает на вход длинную строку с множеством слов.
#      Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
#      функция должна вместо всех символов после шестого поставить одну звездочку.
#      Пример: Из слова 'verwijdering' должно получиться 'verwij*'

def shortener(string):
    return " ".join(map(lambda w: w if len(w) < 6 else w[:6] + "*", s.split()))




