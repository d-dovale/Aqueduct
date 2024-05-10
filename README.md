# Aqueduct

## About the Project

The "Aqueduct" project is designed to solve a unique problem of directing water through a grid-based system efficiently. The objective is to calculate the minimum cost of a supply path from a source station, visiting all specified bathhouses, and potentially ending at any of them. The challenge is facilitated through a grid where stations have varying heights, affecting the time and cost to move between them based on these differences.

### Built With

* ![Python]

## Algorithms Implemented

### Bellman-Ford Algorithm

- The Bellman-Ford algorithm is implemented to determine the shortest path from the source station to all other stations in the graph. This forms the basis for calculating the minimum cost of visiting all specified bathhouses. The algorithm is particularly useful in graphs where edge weights may be negative but no negative weight cycles exist.

- **Time Complexity**: $O(V*E)$, where $V$ is the number of vertices and $E$ is the number of edges. This complexity stems from checking all edges of the graph for each vertex.

### Dynamic Programming with Memoization

- A recursive function with memoization, named `opt`, is designed to compute the minimum path cost. It takes two parameters: the current station and a set of remaining bathhouses. The function uses memoization to store results of subproblems, thus avoiding redundant calculations and significantly reducing the time complexity.

- **Recursive Equation:** Given a set of remaining bathhouses B and a current station s, the function opt is defined as follows:

    - $opt(s, B) = min_{b in B} (dist(s, b) + opt(b, B \setminus {b}))$

    - Where $dist(s, b)$ is the shortest distance from station $s$ to bathhouse $b$, which can be computed using the Bellman-Ford algorithm. This recursion terminates when $B$ is empty, at which point $opt(s, \emptyset) = 0.$

- **Time Complexity**: $O(2^B * B^2)$, where $B$ is the number of bathhouses. This accounts for each subset of bathhouses and every possible next bathhouse in the path.

## How to Run

To run the "Aqueduct" project, follow these steps:

1. Ensure Python is installed on your system.
2. Place your `grid.txt` file in the outer-most directory as the script or modify the path in the `main` function accordingly.
3. Run the script using a Python interpreter:

```bash
python aqueduct.py
```

## Expected Input Format
The input should be in a text file `grid.txt` with the following format:

- **First line:** grid dimensions $m$,$n$
- **Following lines:** height, $x$, $y$ for each station
- **Line after the last station:** $source_x$, $source_y$
- **Remaining lines:** $bathhouse_x$, $bathhouse_y$ for each bathhouse

### Example Usage

- Below is an example `grid.txt` file that is given in the repository
- When `aqueduct.py` is run, the correct output file `pathLength.txt` should be 48 which represents the shortest path from the source node (0,0) to all the bathhouses

```
7, 9
7, 0, 0
22, 1, 0
17, 2, 0
4, 3, 0
9, 4, 0
9, 5, 0
10, 6, 0
5, 0, 1
9, 1, 1
16, 2, 1
25, 3, 1
9, 4, 1
21, 5, 1
8, 6, 1
23, 0, 2
12, 1, 2
5, 2, 2
23, 3, 2
8, 4, 2
11, 5, 2
18, 6, 2
21, 0, 3
24, 1, 3
2, 2, 3
7, 3, 3
10, 4, 3
1, 5, 3
9, 6, 3
7, 0, 4
5, 1, 4
14, 2, 4
22, 3, 4
9, 4, 4
2, 5, 4
14, 6, 4
22, 0, 5
1, 1, 5
3, 2, 5
23, 3, 5
3, 4, 5
25, 5, 5
25, 6, 5
24, 0, 6
15, 1, 6
19, 2, 6
0, 3, 6
13, 4, 6
12, 5, 6
1, 6, 6
19, 0, 7
6, 1, 7
20, 2, 7
14, 3, 7
0, 4, 7
25, 5, 7
21, 6, 7
0, 0, 8
21, 1, 8
4, 2, 8
6, 3, 8
1, 4, 8
19, 5, 8
11, 6, 8
4, 6
6, 0
1, 4
2, 0
2, 4
0, 2
```

## Contributors

Daniel Dovale - ddovale2004@gmail.com

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white