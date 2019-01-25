# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
from random import randint
lst1 = [randint(-10, 10) for i in range(10)]
print(lst1)
lst2 = [i**2 for i in lst1]
print(lst2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits1 = ['mango', 'apple', 'banana', 'peach']
fruits2 = ['mango', 'apple', 'banana', 'peach', 'orange']
fruits = [i for i in fruits1 if i in fruits2]
print(fruits)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

from random import randint
lst1 = [randint(-10, 10) for i in range(10)]
print(lst1)
lst2 = [i for i in lst1 if (i % 3 == 0) and (i > 0) and (i % 4 != 0)]
print(lst2)