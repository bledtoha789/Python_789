##Задача №3459. Дележ яблок - 2
##n  школьников делят k яблок поровну, неделящийся остаток остается 
##в корзинке. Сколько яблок останется в корзинке?
n = int(input('Введите количество школников '))
k = int(input('Введите количество яблок '))
c = k // n
print('Яблок осталось в корзинке', c)