def SmejToSmejList(vertex_num, smejnost_matrix):
    smejnost_lists = [[i] for i in range(vertex_num)]  # создание списка смежности с номерами вершин
    for i in range(len(smejnost_matrix)):
        for j in range(len(smejnost_matrix[i])):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # если найдена смежная вершина
                smejnost_lists[i].append([j, smejnost_matrix[i][j] if smejnost_matrix[i][j] != 2 else 1])  # добавить в список смежности пару в формате [вершина, вес]
    return smejnost_lists


def VGubinu(smejnost_list):  # функция прохода в глубину
    out = []  # результирующий список
    stek = []  # стек для реализации прохода в глубну
    cur = 0  # номер текущей вершины
    for i in range(len(smejnost_list)):
        if len(smejnost_list[i]) != 0:  # выбор такой текущей вершины, чтобы она была смежна с хотябы еще одной вериной
            cur = i
            break
    out.append(cur)  # ввод начальной вершины в результирующий список и стек
    stek.append(cur)
    out_fl = True  # флаг выхода из цикла
    while out_fl:
        for i in smejnost_list[cur]:
            if i not in out:
                cur = i  # выбор новой вершины еще не записанной в результирующий список
                break
        if cur in out:  # если на предыдущем шаге не найдена не использованная вершина вернутья на предыдущую вершину через стек
            if len(stek) == 0:  # если при этом стек пуст завершить цикл
                out_fl = False
                continue
            cur = stek.pop()
        else:  # иначе добавить новую вершину в результирующий список и стек
            out.append(cur)
            stek.append(cur)
    print("".join(str(i) for i in out))  # вывод результата прохода в глубину


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
    print("".join(str(i) for i in out))  # вывод результата прохода в ширину


def main():
    vertex_num = int(input("Введите количество вершин: "))  # запрос навведенение количества вершин
    print("Введите матрицу смежности:")
    smejnost_matrix = [[int(i) for i in input().split()] for j in range(vertex_num)]  # ввод матрицы смежности с клавиатуры
    smejnost_list_temp = SmejToSmejList(vertex_num, smejnost_matrix)
    smejnost_list = []
    for i in range(vertex_num):
        temp_list = []
        for j in range(1, len(smejnost_list_temp[i])):
            temp_list.append(smejnost_list_temp[i][j][0])  # изменение структуры списка смежности из предыдущих работ
        smejnost_list.append(temp_list)
    print("Обход в ширину: ", end='')
    VGubinu(smejnost_list)
    print("Обход в глубину: ", end='')
    VShirinu(smejnost_list)


main()
""" пример
5
0 1 0 0 1
1 0 1 1 1
0 1 0 1 0
0 1 1 0 1
1 1 0 1 0
"""