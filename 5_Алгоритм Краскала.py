def SmejToSmejList(vertex_num, smejnost_matrix):
    smejnost_lists = [[i] for i in range(vertex_num)]  # создание списка смежности с номерами вершин
    for i in range(len(smejnost_matrix)):
        for j in range(len(smejnost_matrix[i])):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # если найдена смежная вершина
                smejnost_lists[i].append([j, smejnost_matrix[i][j] if smejnost_matrix[i][j] != 2 else 1])  # добавить в список смежности пару в формате [вершина, вес]
    return smejnost_lists


def ToNevzvesh(smejnost_list):  # функция перевода взвешенных списков смежности в невзвешанные
    out = []
    for i in smejnost_list:
        temp_list = []
        for j in i:
            temp_list.append(j[0])  # преобразование пары (вершина, вес) в просто элемент вершина
        out.append(temp_list)
    return out


def VShirinu(smejnost_list):  # функция прохода в ширину
    out = []  # результирующий список
    queue = []  # очередь для реализации прохода в ширину
    cur = 0  # номер текущей вершины
    for i in range(len(smejnost_list)):
        if len(smejnost_list[i]) != 0:  # выбор такой текущей вершины, чтобы она была смежна с хотябы еще одной вериной
            cur = i
            break
    queue.append(cur)  # добавление вершины в очередь
    while len(queue) != 0:
        cur = queue.pop(0)  # получение вершины из начала очереди
        for i in smejnost_list[cur]:  # проход по смежным с текущей вершинам
            if i not in queue and i not in out:  # если вершины нет в результирующем списке и в очереди то добавить ее в очередь
                queue.append(i)
        out.append(cur)  # добавлен е текущей вершины в результирующий список
    return out # вывод результата прохода в ширину


def ToEdgeList(smejnost_list):  # функция создания списка ребер из списков смежности  в элементами в формате [ребро1, ребро2, вес]
    edge_list = []
    for i in range(len(smejnost_list)):
        for j in smejnost_list[i]:
            if [i, j[0], j[1]] not in edge_list and [j[0], i, j[1]] not in edge_list:
                edge_list.append([i, j[0], j[1]])
    return edge_list


def Kraskal(smejnost_list):  # алгоритм Краскала
    edge_list = ToEdgeList(smejnost_list)  # создание списка ребер
    edge_list.sort(key=lambda x: x[-1], reverse=True)  # сортировка списка ребер по убыванию веса
    nevzvesh_list = ToNevzvesh(smejnost_list)  # создание невзвешаннго списка смежности
    for i in edge_list:  # проход по всем ребрам от максимального веса до минимального
        temp_copy = []
        for j in range(len(nevzvesh_list)):
            temp = []
            for t in nevzvesh_list[j]:
                if (i[0] == j and i[1] == t) or (i[1] == j and i[0] == t):  # создание копии невзвешаннго списка смежности без текщего ребра
                    continue
                else:
                    temp.append(t)
            temp_copy.append(temp)
        if len(VShirinu(temp_copy)) == len(smejnost_list):  # если при удалении ребра связности не нарушилась то изменяем начальный невзвешанный список смежности
            nevzvesh_list = temp_copy.copy()
    kraskal = []  # когда ребра закончатся заполняем выходно список ребер
    for i in range(len(nevzvesh_list)):  # проход по всем вершинами и ребрам
        for j in edge_list:
            if j[0] == i and any(map(lambda x: x == j[1], nevzvesh_list[i])):  # если удовлетворяющее ребро найдено вводим его в результирующий список
                kraskal.append(j)
    print("Минимальный остов состоит из:")
    print("\n".join(f"Ребро {(i[0], i[1])} весом: {i[2]}" for i in kraskal))  # вывод результата работы алгоритма Краскала


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
            temp_list.append(smejnost_list_temp[i][j])  # изменение структуры списка смежности из предыдущих работ
        smejnost_list.append(temp_list)
    Kraskal(smejnost_list)


main()
""" пример
5
0 15 0 0 5
15 0 10 6 3
0 10 0 18 0
0 6 18 0 7
5 3 0 7 0
"""