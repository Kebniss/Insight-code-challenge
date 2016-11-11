from nose.tools import *
from Graph import Graph

def test_graph():

    graph = Graph()
    assert_equal(graph.g, {})


def test_add_edge():

    graph1 = Graph()

    graph1.add_edge('a', 'b')
    assert_equals(graph1.g, {'a':set(['b']), 'b':set(['a'])})

    graph1.add_edge('b','c')
    assert_equals(graph1.g, {'a':set(['b']),
                             'b':set(['a', 'c']),
                             'c':set(['b'])
                             }
                  )

    graph1.add_edge('e','d')
    assert_equals(graph1.g, {'a':set(['b']),
                             'b':set(['a', 'c']),
                             'c':set(['b']),
                             'e':set(['d']),
                             'd':set(['e'])
                             }
                  )

    graph1.add_edge('e','d')
    assert_equals(graph1.g, {'a':set(['b']),
                             'b':set(['a', 'c']),
                             'c':set(['b']),
                             'e':set(['d']),
                             'd':set(['e'])
                             }
                  )

    graph2 = Graph()
    assert_equal(graph2.g, {})

    graph2.add_edge('a', 'b')
    assert_equals(graph2.g, {'a':set(['b']), 'b':set(['a']) } )


def test_adj():

    graph = Graph()
    graph.add_edge('a', 'b')
    graph.add_edge('b','c')
    graph.add_edge('e','d')

    assert_equals(Graph.adj(graph,'a'), set(['b']))
    assert_equals(Graph.adj(graph,'b'), set(['a', 'c']))


def test_exists_edge():

    graph1 = Graph()
    graph1.add_edge('a','b')
    graph1.add_edge('b','c')
    graph1.add_edge('e','d')
    assert_equals(graph1.exists_edge('a','a'), True)
    assert_equals(graph1.exists_edge('a','b'), True)
    assert_equals(graph1.exists_edge('a','c'), False)
    assert_equals(graph1.exists_edge('a','h'), False)

def test_bfs():

    graph1 = Graph()
    graph1.add_edge('a','b')
    graph1.add_edge('b','c')
    graph1.add_edge('e','d')
    graph1.add_edge('c','h')
    graph1.add_edge('h','f')
    assert_equals(graph1.bfs_until('a','a', 0), True)
    assert_equals(graph1.bfs_until('a','a', 1), True)
    assert_equals(graph1.bfs_until('a','b', 1), True)
    assert_equals(graph1.bfs_until('a','c', 2), True)
    assert_equals(graph1.bfs_until('a','h', 3), True)
    assert_equals(graph1.bfs_until('a','f', 2), False)
    assert_equals(graph1.bfs_until('a','e', 10), False)

    graph1.add_edge('a', 'h')
    assert_equals(graph1.bfs_until('a','h', 1), True)


def test_bi_bfs():

    graph1 = Graph()
    graph1.add_edge('a','b')
    graph1.add_edge('b','c')
    graph1.add_edge('e','d')
    graph1.add_edge('c','h')
    graph1.add_edge('h','f')
    assert_equals(graph1.bi_bfs_until('a','b', 1), True)
    assert_equals(graph1.bi_bfs_until('a','c', 2), True)
    assert_equals(graph1.bi_bfs_until('a','h', 3), True)
    assert_equals(graph1.bi_bfs_until('a','h', 2), False)
    assert_equals(graph1.bi_bfs_until('a','f', 2), False)
    assert_equals(graph1.bi_bfs_until('a','e', 10), False)

    graph1.add_edge('a', 'h')
    assert_equals(graph1.bfs_until('a','h', 1), True)


def test_are_connected():

    graph1 = Graph()
    graph1.add_edge('a','b')
    graph1.add_edge('c','g')
    graph1.add_edge('i','l')
    graph1.add_edge('e','d')
    graph1.add_edge('h','f')
    graph1.add_edge('m','n')

    assert_equals(graph1.are_connected('a','b'), True)
    assert_equals(graph1.are_connected('c','h'), False)

    graph1.add_edge('c','h')
    assert_equals(graph1.are_connected('c','h'), True)

    assert_equals(graph1.are_connected('a','h'), False)
    graph1.add_edge('b','c')
    assert_equals(graph1.are_connected('a','h'), True)

    assert_equals(graph1.are_connected('m','d'), False)
    graph1.add_edge('n','e')
    assert_equals(graph1.are_connected('m','d'), True)

    graph1.add_edge('i','a')
    graph1.add_edge('d','g')

    assert_equals(graph1.are_connected('m','l'), True)
