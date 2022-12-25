from math import log2


def ToPython(txt_func):  # функция преобразования фулевой функции в читаемую питоном строку длф функции eval
    py_txt_func = []
    for i in txt_func:
        if i == '-':
            py_txt_func.append('not')  # замена - на not
        elif i == '*':
            py_txt_func.append('and')  # замена * на and
        elif i == '+':
            py_txt_func.append('or')   # замена + на or
        elif i == '>':
            if py_txt_func[-1] != ')':
                py_txt_func.insert(-1, 'not')   # замена > на not x or, с поддержкой скобок
            else:
                py_txt_func.insert(len(py_txt_func) - py_txt_func[::-1].index('(') - 1, 'not')
            py_txt_func.append('or')
        elif i == '=':
            py_txt_func.append('==')   # замена = на ==
        else:
            py_txt_func.append(i)   # не заменяет скобки и переменные
    return py_txt_func


def TableOut(res_list):
    n_val = round(log2(len(res_list)))
    header = 'abcdef'[:n_val]
    print(' | '.join(i for i in header) + ' | result')
    for i in range(len(res_list)):
        print(' | '.join(str(i) for i in bin(i)[2:].rjust(n_val, '0')) + f' | {res_list[i]}')


def main():
    txt_func = input("Введите логическое выражение "
                     "(a,b,c,d,e,f: допустимые переменные; -: отрицание; *: коньюнкция; +: дизъюнкция"
                     ">: импликация; =: эквивалентнсть)\n"
                     "Для корректной работы испольуйте только указанные переменные в такойже последовательности\n"
                     "Например для функци 2 переменных используйте только a,b, но не c,d\n")  # ввод функции с пояснениями
    py_txt_func = ' '.join(ToPython(txt_func))  # преобразование списка в строку
    n_val = sum([1 if txt_func.count(i) else 0 for i in 'abcdef'])  # подсчет количества использованных переменных
    res_list = list()  # результирующий список
    val = [False, True]  # список заначений кахждой переменной
    for a in val:
        if n_val == 1:
            res = eval(py_txt_func)  # исполнение строки как кода python функцией eval
            res_list.append(int(res))
            continue
        for b in val:
            if n_val == 2:
                res = eval(py_txt_func)
                res_list.append(int(res))
                continue
            for c in val:
                if n_val == 3:
                    res = eval(py_txt_func)
                    res_list.append(int(res))
                    continue
                for d in val:                      # куча циклов для всех возможных 6 переменных
                    if n_val == 4:
                        res = eval(py_txt_func)
                        res_list.append(int(res))
                        continue
                    for e in val:
                        if n_val == 5:
                            res = eval(py_txt_func)
                            res_list.append(int(res))
                            continue
                        for f in val:
                            if n_val == 6:
                                res = eval(py_txt_func)
                                res_list.append(int(res))

    print('Выражение функции для python:', py_txt_func)
    TableOut(res_list)


main()
"""
пример
(a+b)>c*-(d*c)*a
"""