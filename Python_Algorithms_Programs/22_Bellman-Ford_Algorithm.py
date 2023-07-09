class Graph:
    def __init__(self, Vertices):
        self.M = Vertices  # Total number of Vertices in the Graph
        self.graph = []  # Array of edges

    def add_edge(self, a, b, c): # Adding edges to the graph
        self.graph.append([a, b, c])

    def print_solution(self, distance):
        print("Vertex \t\t Distance from the source")
        for k in range(self.M):
            print(" {0}\t\t\t{1}".format(k, distance[k]))

    def Bellman_Ford(self, src):
        distance = [float("Inf")] * self.M
        distance[src] = 0

        for _ in range(self.M - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c

        for a, b, c in self.graph:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                print("Graph contains negative weight cycle")
                return
            
        self.print_solution(distance)

g = Graph(5)
g.add_edge(0, 1, 2)        
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 2)
g.add_edge(2, 4, 3)
g.add_edge(4, 3, -5)

g.Bellman_Ford(0)

