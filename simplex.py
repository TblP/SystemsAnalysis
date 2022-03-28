import numpy as np


# Функция поиска минимального значения в строчке функции
def min_of_F(d):
    return min(d[0])


# Функция поиска индекса разрешающего столбца
def enable_column(d):
    return list(d[0]).index(min_of_F(d))


# Функция поиска индекса разрешающей строки
def enable_string(d, len_of_strings):
    ratio = []  # Последней столбец симплексной таблицы, отражающей соотношение bi к соответствующему элементу разрешающего столбца
    for i in range(len_of_strings):
        ratio.append(d[i][-1] / d[i][enable_column(d)])
    m = max(ratio)
    m_index = ratio.index(m)  # Защита от одинаковых элементов в ratio
    for i in range(len_of_strings):  # Поиск минимального положительного значения в последнем столбце симплексной таблицы
        ri = ratio[i]
        if 0 < ri < m:
            m = ri
            m_index = i
    return m_index


# Поиск разрешающего элемента
def enable_element(d, len_of_strings):
    return d[enable_string(d, len_of_strings)][enable_column(d)]


# Обнуление всех элементов разрешающего столбца, за исключением элемента разрешающей строки
def column_processing(len_of_strings, len_of_columns):
    global d
    en_str = enable_string(d, len_of_strings)  # Индекс разрешающей строки
    en_col = enable_column(d)  # Индекс разрешающего столбца
    en_el = d[en_str][en_col]  # Значение разрешающего элемента
    result_d = []  # Измененная симплексная таблица
    for i in range(len_of_strings):
        if i != en_str:
            processing_line = list(d[i])  # Обрабатываемая строка
            k = d[i][en_col] / en_el  # Коэффициент домножения разрешающей строки
            for j in range(len_of_columns):  # Вычитание из всех элементов обрабатываемой строки соответствующих элементов разрешающей строки, домноженных на полученный коэффициент
                processing_line[j] = processing_line[j] - k * d[en_str][j]
            result_d.append(processing_line)
        else:  # Добавление неизменяемой разрешающей строки
            result_d.append(list(d[en_str]))
    d = result_d  # Обновление симплексной таблицы


def solve(len_of_strings, len_of_columns):
    global d
    while True:
        if min(list(d[0])) >= 0:  # Выполняем предыдущую функцию до того момента, пока в строке функции все элементы не перестанут быть отрицательными
            break
        else:
            column_processing(len_of_strings, len_of_columns)


# Функция определения базиса (иксы, являющиеся решением и их количество)
def determinate_of_basis(len_of_strings, len_of_columns):
    basis = ""
    len_of_basis = len_of_columns - len_of_strings
    for i in range(len_of_basis):
        basis += "x" + str(i + 1) + " "
    return len_of_basis, basis


# Функция определния коэффициентов, стоящих у базисных переменных
def found_odds_of_nonzero_element(d, basis, len_of_strings):
    odds = [0] * basis
    for i in range(len_of_strings):
        for j in range(basis):
            if d[i][j] != 0:
                odds[j] = d[i][j]
    return odds


def printSol(d, len_of_strings, len_of_columns):
    for i in range(len_of_strings):
        print(d[i])
    bas = determinate_of_basis(len_of_strings, len_of_columns)
    basis = bas[0]
    odds = found_odds_of_nonzero_element(d, basis, len_of_strings)
    print("Базисными переменными являются:", bas[1])
    print("Максимальное значение функции:", d[0][-1])
    print("Максимум функции достигается при значениях:", end="")
    for i in range(basis):
        print("x" + str(i + 1) + " = " + str(d[i + 1][-1] / odds[i]) + "; ", end="")


d = testo = [3,6,102,4,3,91,5,2,105,7,9]
len_of_strings, len_of_columns = d.shape
solve(len_of_strings, len_of_columns)
printSol(d, len_of_strings, len_of_columns)