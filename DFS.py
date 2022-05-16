graph={
    '1': ['2','3'],
    '2': ['4','5'],
    '3': ['6','7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

visited=set()       

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)

# Driver code

dfs(visited, graph, '1')