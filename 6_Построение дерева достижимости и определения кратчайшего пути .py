def SmejToSmejList(vertex_num, smejnost_matrix):
    smejnost_lists = [[i] for i in range(vertex_num)]  # создание списка смежности с номерами вершин
    for i in range(len(smejnost_matrix)):
        for j in range(len(smejnost_matrix[i])):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # если найдена смежная вершина
                smejnost_lists[i].append([j, smejnost_matrix[i][j] if smejnost_matrix[i][j] != 2 else 1])  # добавить в список смежности пару в формате [вершина, вес]
    return smejnost_lists


def SimpleCep(vertex_start, length, smejnost_list, dict_of_chains, vertex_num):  # функция нахождения простых цепей
    chain = [vertex_start]  # масив депи с изначально заданной ставтовой вершиной
    chains = []  # массив всех цепей
    if (vertex_start, length) in dict_of_chains:  # если кортеж из стартовой вершины и данной длинны уже есть в словаре цепей то вывести его
        return dict_of_chains[(vertex_start, length)]
    if length == 1:  # добавление цепей в список если длинна цепи равна 1 (фактически переписывание списка смежности для каждой вершины в удобном формате)
        for i in range(vertex_num):
            if i in smejnost_list[vertex_start] and vertex_start != i:
                for j in range(smejnost_list[vertex_start].count(i)):
                    chain.append(i)
                    chains.append(chain)
                    chain = [vertex_start]
        dict_of_chains[(vertex_start, length)] = chains  # добавление цепей длинны 1 в словарь цепей
        return chains
    else:
        for i in range(vertex_num):  # проход по всем вершинам
            if i in smejnost_list[vertex_start] and vertex_start != i:  # проверка на то что статовая вершина не равна i для избежания лишних операций
                for j in range(smejnost_list[vertex_start].count(i)):
                    for k in SimpleCep(i, length - 1, smejnost_list, dict_of_chains, vertex_num):  # рекурсивный вызов функции с уменьшением длины цепей
                        if vertex_start not in k:
                            chain = [vertex_start] + k
                            chains.append(chain)
                            chain = []
        dict_of_chains[(vertex_start, length)] = chains  # добавление цепей в словарь цепей
        return chains


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


def MinWay(dict_of_chains, edge_list, start_vertex, end_vertex):
    ways = []  # список путей
    key_list = dict_of_chains.keys()  # список ключей словаря простых цепей
    for i in key_list:
        for j in dict_of_chains[i]:  # проход по всем цепям
            if j[0] == start_vertex and j[-1] == end_vertex:  # если начальная и конечная вершины совпадают с заданными
                ways.append(j)  # вводим эту цепь в список путей
    min_way = (-1, [-1])  # минимальный путь
    for way in ways:  # проход по всем путям найденным выше
        len_way = 0  # длина пути
        for i in range(len(way) - 1):  # проходим по вершинам пути и через словарь ребер добавляем их вес в длину пути
            if (way[i], way[i+1]) in edge_list:  # т.к. в словаре ребро указно в одном направлении проверяем оба направления
                len_way += edge_list[(way[i], way[i+1])]
            else:
                len_way += edge_list[(way[i+1], way[i])]
        if min_way[0] == -1 or min_way[0] > len_way:  # если путь окажется меньше чем найденный ранее минимум
            min_way = (len_way, way)  # то записываем длинну пути и сам путь в минимум
    print(f"Длина минимального пути, из вершины {start_vertex} в вершину {end_vertex}, равна: {min_way[0]}")
    print("Путь:", "-".join(str(i) for i in min_way[1]))  # красивыйй вывод минимального пути


def main():
    vertex_num = int(input("Введите количество вершин: "))  # запрос навведенение количества вершин
    print("Введите матрицу смежности:")
    smejnost_matrix = [[int(i) for i in input().split()] for j in
                       range(vertex_num)]  # ввод матрицы смежности с клавиатуры
    smejnost_list_temp = SmejToSmejList(vertex_num, smejnost_matrix)
    smejnost_list_v = []  # создание взвешанного списка смежности
    for i in range(vertex_num):
        temp_list = []
        for j in range(1, len(smejnost_list_temp[i])):
            temp_list.append(smejnost_list_temp[i][j])  # изменение структуры списка смежности из предыдущих работ
        smejnost_list_v.append(temp_list)
    edge_list = ToEdgeList(smejnost_list_v)  # создание списа ребер
    smejnost_list_nv = ToNevzvesh(smejnost_list_v)  # создание невзвешанного списка смености
    simple_cep_list = []  # список простых цпей
    dict_of_chains = dict()  # словарь цепей
    for i in range(vertex_num):
        for j in range(vertex_num - 1, 1, -1):
            simple_cep_list.append(SimpleCep(i, j, smejnost_list_nv, dict_of_chains, vertex_num))  # заполнение списка простых цепей
    start_vertex, end_vertex = [int(i) for i in input("Введите две вешины через пробел: ").split()]  # ввод вершин между которыми надо найти минимальный путь
    MinWay(dict_of_chains, edge_list, start_vertex, end_vertex)


main()
""" пример
5
0 15 0 0 5
15 0 10 6 3
0 10 0 18 0
0 6 18 0 7
5 3 0 7 0
0 3
"""