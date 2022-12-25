def SmejToSmejList(vertex_num, smejnost_matrix):
    smejnost_lists = [[i] for i in range(vertex_num)]  # создание списка смежности с номерами вершин
    for i in range(len(smejnost_matrix)):
        for j in range(len(smejnost_matrix[i])):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # если найдена смежная вершина
                smejnost_lists[i].append([j, smejnost_matrix[i][j] if smejnost_matrix[i][j] != 2 else 1])  # добавить в список смежности пару в формате [вершина, вес]
    return smejnost_lists


def ToEdgeList(smejnost_list):  # функция создания списка ребер из списков смежности  в элементами в формате [ребро1, ребро2, вес]
    edge_list = list()
    for i in range(len(smejnost_list)):
        for j in range(len(smejnost_list[i])):
            if (i, smejnost_list[i][j]) not in edge_list and (smejnost_list[i][j], i) not in edge_list:
                edge_list.append((i, smejnost_list[i][j]))
    return edge_list


def Flery(smejnost_list, in_i=-1, out_i=-1):
    edge_list = ToEdgeList(smejnost_list)  # список ребер
    cur_i = 0  # текущая вершина
    out = []  # результирующий список
    for i in range(len(smejnost_list)):
        if len(smejnost_list[i]) != 0:
            cur_i = i  # выбор такой текущей вершины, чтобы она была смежна с хотябы еще одной вериной
            break
    if in_i != -1:
        cur_i = in_i  # если задана начальная вершина делаем ее текущей
    while len(edge_list) != 0:  # пока в списке ребер есть ребра выполняем алгоритм
        for cur_o in smejnost_list[cur_i]:  # проходим по всем смежным к текущей вершинам
            temp_copy = []
            for i in range(len(smejnost_list)):
                temp = []
                for j in smejnost_list[i]:  # создаем и заполняем копию списка смежности с удаленным ребром (cur_i,cur_o)
                    if not (i == cur_i and j == cur_o) and not (j == cur_i and i == cur_o):
                        temp.append(j)
                temp_copy.append(temp)
            out.append(cur_i)
            if (cur_i, cur_o) in edge_list:
                edge_list.remove((cur_i, cur_o))  # удаляем ребро из списка ребер
            else:
                edge_list.remove((cur_o, cur_i))
            smejnost_list[cur_i].remove(cur_o)  # удаляем вершины ребро из списка смежности
            smejnost_list[cur_o].remove(cur_i)
            cur_i = cur_o  # меняем текщее ребро
            break
    if in_i == -1:
        out.append(out[0])
        print("Эйлеров цикл:\n" + '->'.join(str(i) for i in out))
    else:
        out.append(out_i)
        print("Эйлеров путь:\n" + '->'.join(str(i) for i in out))  # красивы вывод


def main():
    vertex_num = int(input("Введите количество вершин: "))  # запрос навведенение количества вершин
    print("Введите матрицу смежности:")
    smejnost_matrix = [[int(i) for i in input().split()] for j in
                       range(vertex_num)]  # ввод матрицы смежности с клавиатуры
    smejnost_list_temp = SmejToSmejList(vertex_num, smejnost_matrix)
    smejnost_list = []
    for i in range(vertex_num):
        temp_list = []
        for j in range(1, len(smejnost_list_temp[i])):
            temp_list.append(smejnost_list_temp[i][j][0])  # изменение структуры списка смежности из предыдущих работ
        smejnost_list.append(temp_list)
    if all(map(lambda x: len(x) % 2 == 0, smejnost_list)):  # проверка на эйлеров граф
        Flery(smejnost_list)
    elif list(map(lambda x: len(x) % 2 == 0, smejnost_list)).count(False) == 2:  # проверка на полуэйлеров граф
        in_i = list(map(lambda x: len(x) % 2 == 0, smejnost_list)).index(False)  # задание начальной вершины с нечетным количеством смежных вершин
        out_i = list(map(lambda x: len(x) % 2 == 0, smejnost_list)).index(False, in_i + 1)  # задание конечной такойже вершины
        Flery(smejnost_list, in_i=in_i, out_i=out_i)
    else:
        print("Не эйлеров граф")


main()
""" пример цикл
5
0 1 0 0 1
1 0 1 1 1
0 1 0 1 0
0 1 1 0 0
1 1 0 0 0

примеры путь
5
0 1 0 0 1
1 0 1 1 1
0 1 0 1 0
0 1 1 0 1
1 1 0 1 0

5
0 1 0 0 1
1 0 1 0 1
0 1 0 1 0
0 0 1 0 0
1 1 0 0 0
"""
