from Graph import Graph

def feature_1(graph, id_1, id_2):
    if graph.exists_edge(id_1, id_2):
        return 'trusted'
    else:
        return 'unverified'


def feature_2(graph, id_1, id_2):

    distance = graph.bfs_until(id_1, id_2, 2)

    if distance:
        return 'trusted'
    else:
        return 'unverified'


def feature_3(graph, id_1, id_2):

    distance = graph.bfs_until(id_1, id_2, 4)

    if distance:
        return 'trusted'
    else:
        return 'unverified'


def verify_feat1(graph, id_1, id_2):

    distance = graph.bfs_until(id_1, id_2, 1)

    if distance:
        return 'trusted'
    else:
        return 'unverified'

def bi_feature_1(graph, id_1, id_2):
    if graph.bi_bfs_until(id_1, id_2, 1):
        return 'trusted'
    else:
        return 'unverified'


def bi_feature_2(graph, id_1, id_2):
    # TODO HOW ABOUT SELF PAYMENTS?
    if graph.bi_bfs_until(id_1, id_2, 2):
        return 'trusted'
    else:
        return 'unverified'


def bi_feature_3(graph, id_1, id_2):
    # TODO HOW ABOUT SELF PAYMENTS?
    if graph.bi_bfs_until(id_1, id_2, 4):
        return 'trusted'
    else:
        return 'unverified'
