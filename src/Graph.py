"""Class to create and handle graphs"""
from collections import deque

class Graph(object):

    def __init__(self):
        """Initializes the graph to an empty dictionary
        """
        self.g = {}

    def getGraph(self):
        return self.g

    def areConnected(self, v, w):
        """ If v and w are verteces in the grah then check if they are connected
        """
        if v in self.g and w in self.g:
            if w in self.g[v] and v in self.g[w]:
                return True
            else:
                return False
        else:
            return False

    def addEdge(self, v, w):
        """ If any of the two vertex is not in the list add it with the other
            one paired. If any of the two in list and not connected with the
            other connect them
        """
        if v not in self.g:
            self.g[v] = set([])

        self.g[v].add(w)

        if w not in self.g:
            self.g[w] = set([])

        self.g[w].add(v)

    def nVerteces(self):
        """ Returns the number of verteces in a graph2
        """
        if self.g:
            return len(self.g)
        else:
            raise ValueError

    def adj(self, s):
        """ Returns a list with the verteces distant 1 from source s
        """
        return self.g[s]


    def distance_bfs(self, s, t):

        if self.g and (len(self.g) != 0):
            if s in self.g and t in self.g:

                marked = {}.fromkeys(self.g, -1)
                q = deque()
                marked[s] = 0
                q.appendleft((s, marked[s]))

                while len(q) != 0:

                    v, dist = q.pop()

                    for w in self.adj(v):

                        if marked[w] == -1:
                            marked[w] = dist + 1
                            q.appendleft((w, marked[w]))

                        if w == t:
                            return marked[w]

                return "{} and {} are not connected".format(s,t)

            else:
                return "{} and/or {} are not in the graph".format(s,t)

        else:
            raise ValueError
