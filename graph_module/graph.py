from collections import defaultdict

class Graph:
  def __init__(self, connections):
    self.edges = defaultdict(set)
    for edge in connections:
      self.insertEdge(edge[0], edge[1])

  
  def insertEdge(self,u,v):
    self.edges[u].add(v)
    self.edges[v].add(u)
  
  def bfs(self,start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in self.edges[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

  def shortest_path(self, start, end):
    try:
      return next(self.bfs(start, end))
    except StopIteration:
        return None
