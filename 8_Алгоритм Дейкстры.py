def SmejToSmejList(vertex_num, smejnost_matrix):
    smejnost_lists = [[i] for i in range(vertex_num)]  # создание списка смежности с номерами вершин
    for i in range(len(smejnost_matrix)):
        for j in range(len(smejnost_matrix[i])):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # если найдена смежная вершина
                smejnost_lists[i].append([j, smejnost_matrix[i][j] if smejnost_matrix[i][j] != 2 else 1])  # добавить в список смежности пару в формате [вершина, вес]
    return smejnost_lists


def ToEdgeList(smejnost_list):  # функция создания словаря ребер из списков смежности с с элементами по индексам (ребро1б ребро2) и значениями весов
    edge_list = dict()
    for i in range(len(smejnost_list)):
        for j in smejnost_list[i]:
            if (i, j[0]) not in edge_list and (j[0], i) not in edge_list:
                edge_list[(i, j[0])] = j[1]
    return edge_list


def ToNevzvesh(smejnost_list):  # функция перевода взвешенных списков смежности в невзвешанные
    out = []
    for i in smejnost_list:
        temp_list = []
        for j in i:
            temp_list.append(j[0])  # преобразование пары (вершина, вес) в просто элемент вершина
        out.append(temp_list)
    return out


def Deykstra(smejnost_list_v, vertex):
    deykstra = [-1 for _ in range(len(smejnost_list_v))]  # заполнение выходного списка длин -1
    deykstra[vertex] = 0  # длинна заданной вершины 0
    end_flag = True  # флаг выхода из цикла
    cur = vertex  # текущая вершина
    fixed = []  # список зафиксированных длинн вершин
    while end_flag:
        for i in smejnost_list_v[cur]:  # проход по всем смежным с текущей вершинам и заполнение списка длин добавлением весов
            deykstra[i[0]] = i[1] + deykstra[cur] if (i[1] + deykstra[cur]) < deykstra[i[0]] \
                                                     or deykstra[i[0]] == -1 else deykstra[i[0]]
        fixed.append(cur)  # фиксируем текущаю вершину
        cur = min(deykstra[i[0]] if i[0] not in fixed else 100**100 for i in smejnost_list_v[cur])  # проверка на возожности продолжение выполнения алгоритма
        if cur == 100**100:
            end_flag = False
        else:
            cur = deykstra.index(cur)  # замена текущей вершины
    for i in range(len(deykstra)):
        print(f"Минимальный путь из вершины {vertex} в верину {i}: {deykstra[i]}")  # красивый вывод


def main():
    vertex_num = int(input("Введите количество вершин: "))  # запрос навведенение количества вершин
    print("Введите матрицу смежности:")
    smejnost_matrix = [[int(i) for i in input().split()] for j in
                       range(vertex_num)]  # ввод матрицы смежности с клавиатуры
    smejnost_list_temp = SmejToSmejList(vertex_num, smejnost_matrix)
    smejnost_list_v = []
    for i in range(vertex_num):
        temp_list = []
        for j in range(1, len(smejnost_list_temp[i])):
            temp_list.append(smejnost_list_temp[i][j])  # изменение структуры списка смежности из предыдущих работ
        smejnost_list_v.append(temp_list)
    vertex = int(input("Введите вершину: "))  # ввод начальной вершины
    Deykstra(smejnost_list_v, vertex)


main()
""" пример
5
0 15 0 0 5
15 0 10 6 3
0 10 0 18 0
0 6 18 0 7
5 3 0 7 0
0
"""
