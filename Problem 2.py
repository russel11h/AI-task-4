graph1 = {'S': {'A': 1, 'B': 5},
          'A': {'B': 2, 'C': 3, 'D': 4},
          'B': {'D': 3, 'E': 3},
          'C': {'B': 4, 'F': 5},
          'D': {'F': 6},
          'E': {'D': 6, 'G': 10},
          'F': {'G': 5},
          'G': {}
          }

def dfs(start, goal, G):
    expanded = []
    stack = [[start]]

    while stack:
        upath = stack.pop()
        u = upath[-1]

        if u == goal:
            return upath

        if u in expanded:
            continue

        expanded.append(u)

        for v in G[u].keys():
            if v not in expanded:
                vpath = upath + [v]
                stack.append(vpath)

    return None

result = dfs('S', 'G', graph1)
print("Final Path:", "-".join(result))
