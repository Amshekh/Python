graph = {                   # adjacency list  --> for this i'm using Python dictionary
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = set()   # Using set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited

visited = dfs([], graph, '5')
print("Following is Depth-First Search :","\n",visited)
