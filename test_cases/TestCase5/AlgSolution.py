from pathlib import Path
# graph class at top
def open_file(file_name):
    script_dir = Path(__file__).parent
    file_path = script_dir / file_name
    file = open(file_path, "r")
    lines = file.readlines()
    return lines
def create_file(file_name, content):
    script_dir = Path(__file__).parent
    file_path = script_dir / file_name
    file = open(file_path, "w+")
    #check if content is a string
    if type(content) == list:
        for c in content:
            file.write(c)
    else:
        file.write(content)
    file.close()
class Graph:
    def __init__(self, vertices):
        self.M = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges
    
    # Add edges
    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])
    
    # Print the solution
    def print_solution(self, distance):
        print("Vertex Distance from Source")
        for k in range(self.M):
            print("{0}\t\t{1}".format(k, distance[k]))
    
    def bellman_ford(self, src):
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
    def bellman_ford_specific(self, src, target):
        distance = [float("Inf")] * self.M
        distance[src] = 0
        
        for _ in range(self.M - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c
        return(distance[target])
    def print_graph(self):
        print(self.graph)

#First load in the grid.txt file into a set of vertices with x, y, weight 

#Then create a graph with the correct edges and weights using f(q, r) = max(-1, (1+ height(r)-height(q)))

#Finally run the shortest path algorithm on the graph to find the shortest path from the A node touching all B nodes

lines = open_file("grid.txt")

#number of rows and columns is stored in the first line as (rows, columns)
rows, columns = map(int, lines[0].split(','))

#next line until rows * columns are the vertices and their corresponding heights 
heights = []
for i in range(1, rows*columns+1):
    heights.append(int(lines[i].split(',')[0]))

#create mapping from x, y to the vertex number - down rows first then columns. Should be rows * columns vertices
vertex_map = {}
vertex_num = 0
for j in range(columns):
    for i in range(rows):
        vertex_map[(i, j)] = vertex_num
        vertex_num += 1
#now vertexMap is a dictionary with key as (x, y) and value as vertex number
#now store which vertex is A - the next node after the heights - will be a tuple of x, y in the grid and want to use vertex_map to get the actual vertex number
a = tuple(map(int, lines[rows*columns+1].split(',')))
a = vertex_map[a]
#now store which vertices are B - the next nodes after A - will be a list of tuples of x, y in the grid and want to use vertex_map to get the actual vertex number
B = []
for i in range(rows*columns+2, len(lines)):
    B.append(tuple(map(int, lines[i].split(','))))
#convert to vertex numbers
B = [vertex_map[b] for b in B]

#now create the graph with the correct edges and weights
g = Graph(rows*columns)
for i in range(rows):
    for j in range(columns):
        #check if the current vertex is on the edge of the grid
        if i == 0:
            if j == 0:
                #top left corner
                g.add_edge(vertex_map[(i, j)], vertex_map[(i+1, j)], max(-1, (1+ heights[vertex_map[(i+1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j+1)], max(-1, (1+ heights[vertex_map[(i, j+1)]]-heights[vertex_map[(i, j)]])))
            elif j == columns-1:
                #top right corner
                g.add_edge(vertex_map[(i, j)], vertex_map[(i+1, j)], max(-1, (1+ heights[vertex_map[(i+1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j-1)], max(-1, (1+ heights[vertex_map[(i, j-1)]]-heights[vertex_map[(i, j)]])))
            else:
                #top row
                g.add_edge(vertex_map[(i, j)], vertex_map[(i+1, j)], max(-1, (1+ heights[vertex_map[(i+1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j+1)], max(-1, (1+ heights[vertex_map[(i, j+1)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j-1)], max(-1, (1+ heights[vertex_map[(i, j-1)]]-heights[vertex_map[(i, j)]])))
        elif i == rows-1:
            if j == 0:
                #bottom left corner
                g.add_edge(vertex_map[(i, j)], vertex_map[(i-1, j)], max(-1, (1+ heights[vertex_map[(i-1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j+1)], max(-1, (1+ heights[vertex_map[(i, j+1)]]-heights[vertex_map[(i, j)]])))
            elif j == columns-1:
                #bottom right corner
                g.add_edge(vertex_map[(i, j)], vertex_map[(i-1, j)], max(-1, (1+ heights[vertex_map[(i-1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j-1)], max(-1, (1+ heights[vertex_map[(i, j-1)]]-heights[vertex_map[(i, j)]])))
            else:
                #bottom row
                g.add_edge(vertex_map[(i, j)], vertex_map[(i-1, j)], max(-1, (1+ heights[vertex_map[(i-1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j+1)], max(-1, (1+ heights[vertex_map[(i, j+1)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j-1)], max(-1, (1+ heights[vertex_map[(i, j-1)]]-heights[vertex_map[(i, j)]])))
        else:
            if j == 0:
                #left column
                g.add_edge(vertex_map[(i, j)], vertex_map[(i-1, j)], max(-1, (1+ heights[vertex_map[(i-1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i+1, j)], max(-1, (1+ heights[vertex_map[(i+1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j+1)], max(-1, (1+ heights[vertex_map[(i, j+1)]]-heights[vertex_map[(i, j)]])))
            elif j == columns-1:
                #right column
                g.add_edge(vertex_map[(i, j)], vertex_map[(i-1, j)], max(-1, (1+ heights[vertex_map[(i-1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i+1, j)], max(-1, (1+ heights[vertex_map[(i+1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j-1)], max(-1, (1+ heights[vertex_map[(i, j-1)]]-heights[vertex_map[(i, j)]])))
            else:
                #middle vertices
                g.add_edge(vertex_map[(i, j)], vertex_map[(i-1, j)], max(-1, (1+ heights[vertex_map[(i-1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i+1, j)], max(-1, (1+ heights[vertex_map[(i+1, j)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j-1)], max(-1, (1+ heights[vertex_map[(i, j-1)]]-heights[vertex_map[(i, j)]])))
                g.add_edge(vertex_map[(i, j)], vertex_map[(i, j+1)], max(-1, (1+ heights[vertex_map[(i, j+1)]]-heights[vertex_map[(i, j)]])))
#now run the shortest path algorithm on the graph to find the shortest path from the A node touching all B nodes
#save them as it runs in a table - source, vertex, distance
stored_answers = {}
for b in B:
    stored_answers[(a, b)] = g.bellman_ford_specific(a, b)
#now also append distance from each B node to each other B node
for i in range(len(B)):
    for j in range(len(B)):
        if i != j:
            stored_answers[(B[i], B[j])] = g.bellman_ford_specific(B[i], B[j])


def opt(source, vertices, stored_answers):
    #base case - if there are no vertices left
    if len(vertices) == 0:
        return 0
    #if there is only one vertex left
    if len(vertices) == 1:
        return stored_answers[source, vertices[0]]
    #if there are more than one vertex left
    else:
        min_dist = float("Inf")
        for v in vertices:
            new_vertices = vertices.copy()
            new_vertices.remove(v)
            dist = stored_answers[source, v] + opt(v, new_vertices, stored_answers)
            if dist < min_dist:
                min_dist = dist
        return min_dist

#run the opt function with the source as A and the vertices as B. output the int into a file called pathLength.txt
#create the file if it doesn't exist - in the directory the code is located in
create_file("pathLength.txt", str(opt(a, B, stored_answers)))

