INF = 999          # Floyd-Warshall Algorithm  finds shortest path between all the pair of vertices in a weighted graph.
N = 4  # N is the number of Vertices in Graph

G = [[0, 5, INF, INF],
     [50, 0, 15, 5],
     [30, INF, 0, 15],
     [15, INF, 5, 0]]

def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    for r in range(N):
        for p in range(N):
            for q in range(N):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    sol(dist)

def sol(dist):   # To print Output
    for p in range(N):
        for q in range(N):
            if (dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print("\t", dist[p][q], end=" ")
        print(" ")        

floyd(G)        