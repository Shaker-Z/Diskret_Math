from math import log2


def TableOut(res_list):
    n_val = round(log2(len(res_list)))  # определяем кол-во переменных при помощи логарифма
    header = 'abcdef'[:n_val]  # переменные для заглавия таблицы
    print(' | '.join(i for i in header) + ' | result')  # вывод шапки таблицы
    for i in range(len(res_list)):
        print(' | '.join(str(i) for i in bin(i)[2:].rjust(n_val, '0')) + f' | {res_list[i]}')
        # при помощи функции bin преобразовываем номер элемента результирующего списка в двоичную систему и заплняем незначащими нулями до длинны равной кол-ву переменных


def main():
    func = list(map(int, input("Введите элементы результирующего столбца функции чрез пробел (пример: 0 1 0 1)\n").split()))  # ввод элементов
    TableOut(func)


main()
