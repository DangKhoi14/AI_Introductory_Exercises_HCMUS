from collections import defaultdict
from queue import Queue, PriorityQueue

# đọc dữ liệu từ file txt
def read_txt(file):
    size = int(file.readline())
    strat, goal = [int(num) for num in file.readline().split(' ')]
    matrix = [[int(num) for num in line.split(' ')] for line in file]
    return size, strat, goal, matrix
# chuyển ma trận kề thành danh sách kề
def convert_graph(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                adjList[i].append(j)
    return adjList

def convert_graph_weight(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != 0:
                adjList[i].append((j, a[i][j]))
    return adjList

def BFS(graph, start, end):

    visited = []
    frontier = Queue()

    # thêm node start vào frontier và visited
    frontier.put(start)
    visited.append(start)

    # start không có node cha
    parent = dict()
    parent[start] = None

    path_found = False

    while True:
        if frontier.empty():
            raise Exception('No way Exception')
        current_node = frontier.get()
        visited.append(current_node)

        # Kiểm tra current_node có là end hay không
        if current_node == end:
            path_found = True
            break

        for node in graph[current_node]:
            if node not in visited:
                frontier.put(node)
                parent[node] = current_node
                visited.append(node)
        

    # Xây dựng đường đi
    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
    return path

def DFS(graph, start, end):
    visited = []
    frontier = []

    # them node start vào frontier và visited
    frontier.append(start)
    visited.append(start)

    # start không có trong node cha
    parent = dict()
    parent[start] = None

    path_found = False

    while True:
        if frontier == []:
            raise Exception('No way Exception')
        current_node = frontier.pop()
        visited.append(current_node)
        # Kiểm tra current node có là end hay không
        if current_node == end:
            path_found = True
            break

        for node in graph[current_node]:
            if node not in visited:
                frontier.append(node)
                parent[node] = current_node
                visited.append(node)

    # Xây dựng đường đi
    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
    return path

def UCS(graph, start, end):
    
    visited = []
    frontier = PriorityQueue()
    # thêm node start vào frontier và visited
    frontier.put((0, start))
    visited.append(start)
    # start không có node cha
    parent = dict()
    parent[start] = None
    path_found = False
    while True:
        if frontier.empty():
            raise Exception("No way exception")
        current_w, current_node = frontier.get()
        visited.append(current_node)
        # kiểm tra current node có phải là end hay không
        if current_node == end:
            path_found = True
            break
        for nodei in graph[current_node]:
            node, weight = nodei
            if node not in visited:
                frontier.put((current_w + weight, node))
                parent[node] = current_node
                visited.append(node)

    # Xây dựng đường đi
    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
    return current_w, path

if __name__ == '__main__':
    # Đọc file Input.txt và InputUCS.txt
    file_1 = open('Input.txt', 'r')
    file_2 = open('InputUCS.txt', 'r')
    size_1, start_1, goal_1, matrix_1 = read_txt(file_1)
    size_2, start_2, goal_2, matrix_2 = read_txt(file_2)
    file_1.close()
    file_2.close()
    graph_1 = convert_graph(matrix_1)
    graph_2 = convert_graph_weight(matrix_2)

    path_BFS = BFS(graph_1, start_1, goal_1)
    path_DFS = DFS(graph_1, start_1, goal_1)
    current_w, path_UCS = UCS(graph_2, start_2, goal_2)

    print('Found by BFS: ' + ' -> '.join(str(x) for x in path_BFS))
    print('Found by DFS: ' + ' -> '.join(str(x) for x in path_DFS))
    print('Found by UCS: ' + ' -> '.join(str(x) for x in path_UCS) + f'\nCost found by UCS: {current_w}')