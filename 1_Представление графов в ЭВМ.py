def SmejToInced(vertex_num, smejnost_matrix):
    incedentnost_matrix = [[] for i in range(vertex_num)]  # создание пустой матрици инцидентности
    krat_edge_list = [[] for i in range(vertex_num)]  # пустой список кратных верин для дальнейших проверок
    krat_edge_i = 0
    for i in range(vertex_num):
        for j in range(vertex_num):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # поиск смежной вершины
                for l in range(vertex_num):  # если найдена такая вершина заполняем столбец в матрице инцедентности
                    if l == i:
                        incedentnost_matrix[l].append(1)  # добавляем в матрицу инцедентности 1 если это инцедентная вершина
                        if smejnost_matrix[i][j] == 2:  # если это не кратное ребро
                            krat_edge_list[krat_edge_i].append(1)  # записываем в список кратных ребер
                    elif l == j:
                        incedentnost_matrix[l].append(-1)  # добавляем в матрицу инцедентности 1 если это инцедентная вершина
                        if smejnost_matrix[i][j] == 2:  # если это не кратное ребро
                            krat_edge_list[krat_edge_i].append(-1)  # записываем в список кратных ребер
                    else:
                        incedentnost_matrix[l].append(0)  # иначе добавляем 0
                        if smejnost_matrix[i][j] == 2:  # если это не кратное ребро
                            krat_edge_list[krat_edge_i].append(0)  # записываем в список кратных ребер
                krat_edge_i += 1 if smejnost_matrix[i][j] == 2 else 0  # если записалось кратное ребро увеличиваем итератор списка кратных ребер
    incedentnost_matrix = list(zip(*incedentnost_matrix))  # транспонирование матрицы для удаления повторений
    for i in krat_edge_list:
        incedentnost_matrix.append(tuple(i))  # добавление кратных ребер
    i = 0
    while i < len(incedentnost_matrix) - 1:
        t = []
        for j in incedentnost_matrix[i]:  # создание обратноориентированного ребра для дальнейшей проверки
            t.append(-j)
        if tuple(t) in incedentnost_matrix:  # проверка на то что ребро у ориентированного графа двунаправленное
            del (incedentnost_matrix[incedentnost_matrix.index(tuple(t))])  # удаление столбца с ребром в одном раправлении
            incedentnost_matrix[i] = tuple(
                abs(x) for x in incedentnost_matrix[i])  # перезапись столбца с двунаправленным ребром
        else:
            i += 1
    incedentnost_matrix = list(zip(*filter(None, incedentnost_matrix)))  # транспонирование матрицы обратно
    print("\n\nМатрица инцидентности:\n" + '\n'.join(' '.join(str(j) for j in incedentnost_matrix[i]) for i in range(len(incedentnost_matrix))))  # вывод машкицы инцедентности


def SmejToSmejList(vertex_num, smejnost_matrix):
    smejnost_lists = [[i] for i in range(vertex_num)]  # создание списка смежности с номерами вершин
    for i in range(len(smejnost_matrix)):
        for j in range(len(smejnost_matrix[i])):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # если найдена смежная вершина
                smejnost_lists[i].append([j, smejnost_matrix[i][j] if smejnost_matrix[i][j] != 2 else 1])  # добавить в список смежности пару в формате [вершина, вес]
    print("\n\nСписки смежности:\n" + '\n'.join('->'.join(str(j) for j in smejnost_lists[i]) for i in range(len(smejnost_lists))))  # вывод списка смежности


def main():
    vertex_num = int(input("Введите количество вершин: "))  # запрос навведенение количества вершин
    print("Введите матрицу смежности:")
    smejnost_matrix = [[int(i) for i in input().split()] for j in range(vertex_num)]  # ввод матрицы смежности с клавиатуры

    print("Матрица смежности:\n" + '\n'.join(' '.join(str(j) for j in smejnost_matrix[i]) for i in range(vertex_num)))  # вывод матрицы смежности

    SmejToInced(vertex_num, smejnost_matrix)
    SmejToSmejList(vertex_num, smejnost_matrix)


main()
