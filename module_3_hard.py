# Дополнительное практическое задание по модулю: "Подробнее о функциях."

def calculate_structure_sum(*data):
    rez = 0  # переменная для подсчёта общей суммы с учетом рекурсии

    for index_ in data:   # выбираем отдельный элемент на входе
        if isinstance(index_, (int, float)):  # если число
            rez += index_
        elif isinstance(index_, str):  # если строка
            rez += len(index_)
        elif isinstance(index_, dict):  # если словарь
            rez += calculate_structure_sum(index_.items())
        # если список, кортеж или множество(подразумеваем, что нет комплексных чисел и логических значений)
        else:
            rez += calculate_structure_sum(*index_)
    return (rez)


data_structure = [
    [1, 2, 3],  # - список
    {'a': 4, 'b': 5},   # - словарь
    (6, {'cube': 7, 'drum': 8}),   # - кортеж из числа и словаря
    "Hello",  # - строка
    ((), [{(2, 'Urban', ('Urban2', 35))}])]  # - кортеж из кортежа и списка, который из множества в котором список из числа, строки и кортежа, который из строки и числа)
result = calculate_structure_sum(data_structure)
print(result)
