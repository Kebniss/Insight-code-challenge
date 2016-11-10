"""Class to create and handle graphs"""
import math
from collections import deque
from UnionFind import UnionFind

class Graph(object):

    def __init__(self):
        """Initializes the graph to an empty dictionary
        """
        self.g = {}
        self.clusters = UnionFind()

    def exists_edge(self, v, w):
        """ If v and w are vertices in the grah then check if they are connected
        """
        if v in self.g and w in self.g:
            if v == w:
                return True # implicitly it exists edge between a vertex and itself
            if w in self.g[v] and v in self.g[w]:
                return True
            else:
                return False
        else:
            return False

    def add_edge(self, v, w):
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

        self.clusters.union(self.clusters[v], self.clusters[w])

    def adj(self, s):
        """ Returns a list with the vertices distant 1 from source s
        """
        return self.g[s]

    def are_connected(self, v, w):
        return self.clusters[v] == self.clusters[w]


    def bfs_until(self, s, t, limit):
        """ Verifies if the distance between source and target is closer or
            as close as limit.
        """

        if self.g is None or (len(self.g) == 0):
            return False # Empty graph cannot contain s and t

        if s not in self.g or t not in self.g:
            return False # if either one of the two is not in the graph they can't be connected

        if s == t: # implicitly it exists edge between a vertex and itself
            return True

        marked = set([])
        q = deque()
        marked.add(s)
        # append a vertex and its distance from the source
        q.appendleft((s, 0))

        while len(q) > 0:
            v, dist = q.pop()
            if dist >= limit:
                return False
            for w in self.adj(v):
                if w not in marked:
                    if w == t:
                        #print "dist: ", dist
                        return True
                    else:
                        marked.add(w)
                        q.appendleft((w, dist + 1))
        return False


    def bi_bfs_until(self, s, t, limit):
        """ Verifies if the distance between source and target is closer or
            as close as limit.
        """

        if not self.g:
            return False # Empty graph cannot contain s and t

        if not self.are_connected(s, t):
            return False # if either one of the two is not in the graph they can't be connected

        if s == t: # implicitly it exists edge between a vertex and itself
            return True

        marked_s = {}
        marked_t = {}
        q_s = deque()
        q_t = deque()
        marked_s[s] = 0
        marked_t[t] = 0
        # append a vertex and its distance from the source
        q_s.appendleft((s, 0))
        q_t.appendleft((t, 0))
        dist = 0

        while dist < math.ceil(limit * 1.0 / 2):

            while q_s:
                v_s, dist_s = q_s[-1] # peek

                if dist_s > dist:
                    break

                v_s, dist_s = q_s.pop()
                for w_s in self.adj(v_s):
                    if w_s not in marked_s:
                        marked_s[w_s] = dist_s + 1
                        q_s.appendleft((w_s, marked_s[w_s]))

            while q_t:
                v_t, dist_t = q_t[-1] # peek

                if dist_t > dist:
                    break

                v_t, dist_t = q_t.pop()
                for w_t in self.adj(v_t):
                    if w_t not in marked_t:
                        marked_t[w_t] = dist_t + 1
                        q_t.appendleft((w_t, marked_t[w_t]))

            # There may be multiple paths that connect the two vertices
            common_vertices = list(marked_s.viewkeys() & marked_t.viewkeys())
            if len(common_vertices) > 0:
                # We choose the shortest
                min_distance = float("inf")
                for i, v in enumerate(common_vertices):
                    distance = marked_s[v] + marked_t[v]
                    if distance < min_distance:
                        min_distance = distance

                return min_distance <= limit

            dist += 1
        return False
