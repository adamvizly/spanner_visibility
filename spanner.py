def primsAlgorithm(the_graph, number_of_vertices):
    mstMatrix = [[0 for column in range(number_of_vertices)] for row in range(number_of_vertices)]
    positiveInf = 9999999
    selectedVertices = [0 for vertex in range(number_of_vertices)]
    edge_count = 0
    selectedVertices[0] = True

    while edge_count < number_of_vertices-1:
        minimum = positiveInf
        start = 0
        end = 0

        for i in range(number_of_vertices):
            if selectedVertices[i]:
                for j in range(number_of_vertices):
                    if (not selectedVertices[j] and the_graph[i][j]):
                        if the_graph[i][j] < minimum:
                            minimum = the_graph[i][j]
                            start, end = i, j
        selectedVertices[end] = True
        mstMatrix[start][end] = the_graph[start][end]
        mstMatrix[end][start] = mstMatrix[start][end]
        edge_count += 1

    return mstMatrix
