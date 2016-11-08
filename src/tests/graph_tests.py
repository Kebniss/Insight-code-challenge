from nose.tools import *
from Graph import Graph

def test_graph():

    graph = Graph()
    assert_equal(graph.g, {})

def test_getGraph():

    graph = Graph()
    assert_equal(graph.getGraph(), {})

def test_addEdge():

    graph1 = Graph()

    graph1.addEdge('a', 'b')
    assert_equals(graph1.g, {'a':set(['b']), 'b':set(['a'])})

    graph1.addEdge('b','c')
    assert_equals(graph1.g, {'a':set(['b']), 'b':set(['a', 'c']), 'c':set(['b'])})

    graph1.addEdge('e','d')
    assert_equals(graph1.g, {'a':set(['b']),
                             'b':set(['a', 'c']),
                             'c':set(['b']),
                             'e':set(['d']),
                             'd':set(['e'])})

    graph1.addEdge('e','d')
    assert_equals(graph1.g, {'a':set(['b']),
                             'b':set(['a', 'c']),
                             'c':set(['b']),
                             'e':set(['d']),
                             'd':set(['e'])})

    graph2 = Graph()
    assert_equal(graph2.g, {})

    graph2.addEdge('a', 'b')
    assert_equals(graph2.g, {'a':set(['b']), 'b':set(['a'])})


def test_nVerteces():

    graph = Graph()
    graph.addEdge('a', 'b')
    graph.addEdge('b','c')
    graph.addEdge('e','d')

    assert_equals(graph.nVerteces(), 5)


def test_adj():

    graph = Graph()
    graph.addEdge('a', 'b')
    graph.addEdge('b','c')
    graph.addEdge('e','d')

    assert_equals(Graph.adj(graph,'a'), set(['b']))
    assert_equals(Graph.adj(graph,'b'), set(['a', 'c']))


def test_bfs():

    graph1 = Graph()
    graph1.addEdge('a','b')
    graph1.addEdge('b','c')
    graph1.addEdge('e','d')
    assert_equals(graph1.distance_bfs('a','b'), 1)
    assert_equals(graph1.distance_bfs('a','c'), 2)
    assert_equals(graph1.distance_bfs('a','g'), "a and/or g are not in the graph")
    assert_equals(graph1.distance_bfs('g','a'), "g and/or a are not in the graph")
    assert_equals(graph1.distance_bfs('a','e'), "a and e are not connected")


@raises(ValueError)
def test_nVerteces_exeption():

    graph = Graph()
    graph.nVerteces()


@raises(ValueError)
def test_bfs_exeption():

    graph = Graph()
    graph.distance_bfs('a', 'b')
