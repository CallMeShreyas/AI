graph={
    '1':['2','3'],
    '2':['4','5'],
    '3':['6','7'],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
}

visited=[]      #store visited nodes
queue=[]        #queue for BFS

def bfs(visited, graph, root):
    visited.append(root)
    queue.append(root)

    while queue:
        m = queue.pop(0)
        print(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code

bfs(visited, graph, '1')
