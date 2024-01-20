import random

##Array20. Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N). Найти
##сумму элементов массива с номерами от K до L включительно.

##n = random.randint(10,20)
##l = random.randint(3,n)
##k = random.randint(0,l)
##print("N = ", n)
##print("L = ", l)
##print("K = ", k)
##a = [random.randrange(1,20) for i in range(n)]
##print(a)
##s = 0
##for i in range(k,l+1):
##    s = s + a[i]
##    print(i,":",a[i])
##print("Summa = ",s)

##Array21. Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N).
##Найти среднее арифметическое элементов массива с номерами от K до L
##включительно.

##n = random.randint(10,20)
##l = random.randint(3,n)
##k = random.randint(0,l)
##print("N = ", n)
##print("L = ", l)
##print("K = ", k)
##a = [random.randrange(1,20) for i in range(n)]
##print(a)
##s = 1
##for i in range(k,l+1):
##    s = s + a[i]
##    print(i,":",a[i])
##c = s/(l-k+1)
##print("SrArfm = ",c)

##Array22. Дан массив размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти
##сумму всех элементов массива, кроме элементов с номерами от K до L
##включительно

n = random.randint(10,20)
l = random.randint(3,n)
k = random.randint(1,l)
print("N = ", n)
print("L = ", l)
print("K = ", k)
a = [random.randrange(1,20) for i in range(n)]
print(a)
s = 0
for i in range(1,k+1):
    s = s + a[i]
    print(i,":",a[i])
for i in range(l,n):
    s = s + a[i]
    print(i,":",a[i])
print("Summa = ",s)




