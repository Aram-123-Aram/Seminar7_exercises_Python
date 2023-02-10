'''
Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9. 
При решении задачи используйте комбинацию функций filter, map, sum.
Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
'''
'''
lst = [x for x in range(10,100) if x%9==0]
#print(sum(lst))
sum=0
for x in lst:
    sum+=x
print(sum)
'''
lst = [x for x in range(10, 100)]

lst = list(filter(lambda x: x%9==0,lst))
print(lst)
print(sum(lst))
