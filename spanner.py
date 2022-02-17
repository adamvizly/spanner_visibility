def primsAlgorithm(the_graph, number_of_vertices):
    mstMatrix = [[0 for column in range(number_of_vertices)] for row in range(number_of_vertices)]
    positiveInf = 9999999
    selectedVertices = [False for vertex in range(number_of_vertices)]

    while(False in selectedVertices):
        minimum = positiveInf

        # The starting vertex
        start = 0

        # The ending vertex
        end = 0

        for i in range(number_of_vertices):
            if selectedVertices[i]:
                for j in range(i, number_of_vertices):
                    if (not selectedVertices[j] and the_graph[i][j] > 0.0):
                        if the_graph[i][j] < minimum:
                            minimum = the_graph[i][j]
                            start, end = i, j
        selectedVertices[end] = True
        mstMatrix[start][end] = minimum
        if minimum == positiveInf:
            mstMatrix[start][end] = 0
        mstMatrix[end][start] = mstMatrix[start][end]

    return mstMatrix
