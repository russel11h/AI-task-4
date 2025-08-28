from collections import deque
 
graph = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Eforie': ['Hirsova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Neamt': ['Iasi'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Rimnicu': ['Sibiu', 'Pitesti', 'Craiova'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Zerind': ['Arad', 'Oradea']
}
 
def bfs(start, goal):
    frontier = deque([[start]])
    explored = set()
 
    while frontier:
        path = frontier.popleft()
        node = path[-1]
 
        if node == goal:
            return path
 
        if node not in explored:
            explored.add(node)
            for neighbor in sorted(graph[node]):
                if neighbor not in explored:
                    new_path = path + [neighbor]
                    frontier.append(new_path)
 
print("BFS path:", bfs("Lugoj", "Bucharest"))