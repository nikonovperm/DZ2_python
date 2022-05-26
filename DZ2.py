# 1. Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def sum_of_numbers_in_odd_positions(spisok):
    sum = 0
    for i in range(len(spisok)):
        if i % 2 == 0:
            sum += spisok[i]
    return sum

spisok = [2,4,5,6,7,8]
result = sum_of_numbers_in_odd_positions(spisok)
print(result)

# 2. Найти произведение пар чисел в списке. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; 
# [2, 3, 5, 6] => [12, 15] 

def product_of_pairs_of_numbers_in_list(spisok):
    new_spisok = []
    for i in range(int(len(spisok)/2+0.5)): # +0.5 для учета среднего элемента
        new_spisok.append(spisok[i] * spisok[-(i+1)])
    return new_spisok

spisok = [1,2,3,4,5,6]
print(product_of_pairs_of_numbers_in_list(spisok))

# 3. В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части
#  элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference_of_max_min(spisok):
    min = round((spisok[0] - int(spisok[0])),5)
    max = round((spisok[0] - int(spisok[0])),5)
    #print(max, min)
    for i in range(1, len(spisok)):
        if round((spisok[i] - int(spisok[i])),5) < min and round((spisok[i] - int(spisok[i])),5) !=0:
            min = round((spisok[i] - int(spisok[i])),5)
        elif round((spisok[i] - int(spisok[i])),5) > max:
            max = round((spisok[i] - int(spisok[i])),5)
        #print(max, min)
    difference = round((max - min), 5)
    return difference

spisok = [1.748, 1.2, 3.3, 5, 10.005]
print(difference_of_max_min(spisok)) 

# 4. Написать программу преобразования десятичного числа в 
# двоичное

def decimal_to_binary(decimal):
    binary = ''
    if decimal == 0:
        binary = 0
        return binary
    else:
        while decimal > 0:
            binary = binary + str(decimal % 2)
            decimal = decimal // 2
        return binary[::-1]
    
decimal = int(input(f'Введите десятичное число: '))
print(f'Число {decimal} в двоичном виде: {decimal_to_binary(decimal)}')
