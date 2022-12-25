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
        for j in incedentnost_matrix[i]:
            t.append(-j)
        if tuple(t) in incedentnost_matrix:  # проверка на то что ребро у ориентированного графа ребро двунаправленное
            del (
            incedentnost_matrix[incedentnost_matrix.index(tuple(t))])  # удаление столбца с ребром в одном раправлении
            incedentnost_matrix[i] = tuple(
                abs(x) for x in incedentnost_matrix[i])  # перезапись столбца с двунаправленным ребром
        else:
            i += 1
    return list(zip(*filter(None, incedentnost_matrix)))  # транспонирование матрицы обратно


def SmejToSmejList(vertex_num, smejnost_matrix):
    smejnost_lists = [[i] for i in range(vertex_num)]  # создание списка смежности с номерами вершин
    for i in range(len(smejnost_matrix)):
        for j in range(len(smejnost_matrix[i])):  # проход по матрице смежности
            if smejnost_matrix[i][j] != 0:  # если найдена смежная вершина
                smejnost_lists[i].append([j, smejnost_matrix[i][j] if smejnost_matrix[i][j] != 2 else 1])  # добавить в список смежности пару в формате [вершина, вес]
    return smejnost_lists


def component_find(v, c_num, used, comp, smejnost_list):
    used[v] = True  # вершина с индексом v записывается как использованнная
    comp[v] = c_num  # количество компонент верины v
    for i in smejnost_list[v]:                                   # проходясь по списку смежности для вершины v
        if not used[i]:                                          # если вершина еще не использовалась
            component_find(i, c_num, used, comp, smejnost_list)  # снова запускаем рекурсию поиска всех смежных не использованных вершин


def main():
    vertex_num = int(input("Введите количество вершин: "))  # запрос навведенение количества вершин
    print("Введите матрицу смежности:")
    smejnost_matrix = [[int(i) for i in input().split()] for j in range(vertex_num)]  # ввод матрицы смежности с клавиатуры

    incedentnost_matrix = SmejToInced(vertex_num, smejnost_matrix)  # создание матрицы инцидентности из матрицы смежности
    smejnost_list_temp = SmejToSmejList(vertex_num, smejnost_matrix)  # создание списков смежности из матрицы смежности
    smejnost_list = []
    for i in range(vertex_num):                            #
        temp_list = []                                     #
        for j in range(1, len(smejnost_list_temp[i])):     #
            temp_list.append(smejnost_list_temp[i][j][0])  # преобразование списков смежности для удобства работы
        smejnost_list.append(temp_list)                    #

    used = [[] for _ in range(100)]  # список используемых вершин
    comp = [[] for _ in range(100)]  # список компонент связности
    c_num = 1
    for i in range(vertex_num):  # в цикле идем по всем вершинам
        if not used[i]:  # если нершина не испрользована
            component_find(i, c_num, used, comp, smejnost_list)  # заходим в рекурсивную функцию нахождения всех связанных вершин
            c_num += 1
    comp = max(list(filter(None, comp)))  # после работы цикла число компонент равно максимуму в списке comp
    print("Число компонент сязности: " + str(comp))
    print(f"Оценка числа ребер(q) через число вершин и число компонент связности: {vertex_num - comp} <= q <= "
          f"{(vertex_num - comp)*(vertex_num - comp + 1) / 2}")
    if incedentnost_matrix:                                        # если матрица инцедентности не пуста
        print("Число ребер: " + str(len(incedentnost_matrix[0])))  # то количество ребер это количество солбцов
    else:
        print("Число ребер: 0")  # иначе количество ребер - 0


main()


""" пример
0 1 1 1
1 0 1 0
1 1 0 0
1 0 0 0
"""
