# Задача 10: 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монеток: "))
r = int(input("Введите количество монеток лежащих вверх решкой: "))
g = n - r
print("Количество монеток лежащих вверх гербом: ", g)
if r > g:
    print("Необходимо перевернуть ", g, " монеток, лежащих вверх гербом")
elif g > r:
    print("Необходимо перевернуть ", r, " монеток, лежащих вверх решкой")
elif g == r:
    print("Необходимо перевернуть любых ", g, " монеток")