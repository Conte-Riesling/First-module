#     '''Function should return something like this:
#     spam(1);#bulochka
#     spam(3);#bulochkabulochkabulochka
#     But it is broken. Fix it please!
#
#     Эта функция принимает числовой параметр. Должна вернуть строку, которая
#     повторяется столько раз, сколько параметров передано. Она уже написана,
#     но не работает. Любым способом заставьте ее работать.

def spam(number):
    return ["bulochka" for i in range(number+1)]

