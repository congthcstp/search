from collections import deque

# BFS from given source s
def bfs(adj, s, visited):
  
    q = deque() # Create a queue for BFS

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    # Iterate over the queue
    while q:
        curr = q.popleft() # Dequeue a vertex
        print(curr, end=" ")

        # Get all adjacent vertices of curr
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True # Mark as visited
                q.append(x) # Enqueue it

def bfs_disconnected(adj):
    visited = [False] * len(adj) # Not visited

    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i, visited)

def dfs_rec(adj, visited, s):
    # Mark the current vertex as visited
    visited[s] = True

    # Print the current vertex
    print(s, end=" ")

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, s):
    visited = [False] * len(adj)
    # Call the recursive DFS function
    dfs_rec(adj, visited, s)

def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)

if __name__ == "__main__":
    # Define the edges of the graph
    edges = [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5]]
    
    V = 0

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]
    # Populate the adjacency list with edges
    while(1):
        try:
            for e in edges:
                add_edge(adj, e[0], e[1])
            break
        except IndexError:
            V+=1
            adj = [[] for _ in range(V)]
            #print(V)

    source = 1
    print("DFS: ")
    dfs(adj, source)
    print("\nBFS : ")
    bfs_disconnected(adj)
