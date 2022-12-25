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


def main():
    vertex_num = int(input("Введите количество вершин: "))  # запрос навведенение количества вершин
    print("Введите матрицу смежности:")
    smejnost_matrix = [[int(i) for i in input().split()] for j in range(vertex_num)]  # ввод матрицы смежности с клавиатуры

    smejnost_list_temp = SmejToSmejList(vertex_num, smejnost_matrix)
    smejnost_list = []
    for i in range(vertex_num):
        temp_list = []
        for j in range(1, len(smejnost_list_temp[i])):  # изменение структуры списка смежности из предыдущих работ
            temp_list.append(smejnost_list_temp[i][j][0])
        smejnost_list.append(temp_list)

    simple_cep_list = []
    dict_of_chains = dict()
    for i in range(vertex_num):
        for j in range(vertex_num - 1, 1, -1):
            simple_cep_list.append(SimpleCep(i, j, smejnost_list, dict_of_chains, vertex_num))  # заполнение списка простых цепей
    length = 0
    for i in list(sorted(dict_of_chains.keys(), key=lambda x: x[1])):
        if i[1] > length:
            length += 1
            print(f"Цепи длиной: {length}")  # красивый вывод всех простых цепей
        print(f"{i[0]}: {'; '.join('-'.join(str(t) for t in j) for j in dict_of_chains[i])}")


main()
""" пример
5
0 1 0 0 1
1 0 1 1 1
0 1 0 1 0
0 1 1 0 1
1 1 0 1 0
"""
