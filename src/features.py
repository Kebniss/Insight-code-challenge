from Graph import Graph

def feature_1(graph, id_1, id_2):
    # TODO HOW ABOUT SELF PAYMENTS?
    if id_1 == id_2 or graph.areConnected(id_1, id_2):
        return 'trusted'
    else:
        return 'unverified'


def feature_2(graph, id_1, id_2):

    distance = graph.distance_bfs(id_1, id_2)

    if distance <= 2:
        return 'trusted'
    else:
        return 'unverified'


def feature_3(graph, id_1, id_2):

    distance = graph.distance_bfs(id_1, id_2)

    if distance <= 4:
        return 'trusted'
    else:
        return 'unverified'


def verify_feat1(graph, id_1, id_2):

    distance = graph.distance_bfs(id_1, id_2)

    if distance <= 1:
        return 'trusted'
    else:
        return 'unverified'
