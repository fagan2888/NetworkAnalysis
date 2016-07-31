import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


def get_circular_dg():
    '''
    Creates a directed graph with 20 integer nodes.
    Every even interger node is connected to the next odd integer node.

    Parameters
    ---------
    None

    Returns
    -------
    A networkx.Digraph instance.
    '''

    dg = nx.DiGraph()
    dg.add_nodes_from(range(20))
    edgs = [(idx, idx + 1) for idx in range(dg.order()) if idx % 2 == 0]
    dg.add_edges_from(edgs)

    return dg


def draw_circular_dg(dg):
    '''
    Draws a directed graph.

    Parameters
    ---------
    dg: A networkx.DiGraph instance.

    Returns
    -------
    A matplotlib.Axes instance.
    '''

    ax = plt.gca()

    nx.draw_circular(dg, with_labels=True, ax=ax)

    return ax


def get_multigraph():
    '''
    Creates an undirected multigraph with five nodes.

    Paramters
    ---------
    None

    Returns
    -------
    A networkx.MultiGraph instance.
    '''

    mg = nx.MultiGraph()
    mg.add_nodes_from(range(5))

    return mg


def draw_multigraph(mg):
    '''
    Draws a multigraph in circular format.

    Paramters
    ---------
    mg: A networkx.MultiGraph instance.

    Returns
    -------
    A matplotlib.Axes instance.
    '''

    ax = draw_circular_dg(mg)

    return ax


def add_edges(mg):
    '''
    Adds new edges between all even integer nodes (0, 2, 4)
    and between all odd integer nodes (1, 3).

    Paramters
    ---------
    mg: A networkx.MultiGraph instance.

    Returns
    -------
    A matplotlib.Axes instance.
    '''

    mg.add_edge(0, 2)
    mg.add_edge(4, 0)
    mg.add_edge(2, 4)
    mg.add_edge(1, 3)

    return mg


def draw_graph(graph):
    '''
    Draws the social network of Zachary's Karate club.

    Paramters
    ---------
    graph: A networkx.Graph instance.

    Returns
    -------
    A matplotlib.Axes instance.
    '''

    ax = plt.gca()

    nx.draw(graph, with_labels=True, ax=ax)

    return ax


def get_degree(graph):
    '''
    Computes the degree of each node.

    Paramters
    ---------
    graph: A networkx.Graph instance.

    Returns
    -------
    A dict of foramt {node: degree}
    '''

    result = dict()

    for node in graph.nodes_iter():
        result[node] = graph.degree(node)

    return result


def draw_graph_friends(graph):
    '''
    Draws the social network of Zachary's Karate club,
    but uses different colors for friends of node 0 and node 33.

    Paramters
    ---------
    graph: A networkx.Graph instance.

    Returns
    -------
    A matplotlib.Axes instance.
    '''

    ax = plt.gca()

    nodes_0 = [0]
    nodes_33 = [33]

    for edge in graph.edges():
        if edge[0] == 0:
            nodes_0.append(edge[1])
        if edge[1] == 33:
            nodes_33.append(edge[0])

    pos = nx.spring_layout(graph)

    nx.draw(graph, pos=pos, with_labels=True, ax=ax)
    nx.draw_networkx_nodes(graph, pos=pos, nodelist=nodes_0, node_color='b', ax=ax)
    nx.draw_networkx_nodes(graph, pos=pos, nodelist=nodes_33, node_color='g', ax=ax)

    return ax


def draw_graph_split(graph):
    '''
    Draws the social network of Zachary's Karate club,
    but uses different colors for two subgroups after the breakup.

    Paramters
    ---------
    graph: A networkx.Graph instance.

    Returns
    -------
    A matplotlib.Axes instance.
    '''

    ax = plt.gca()

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos=pos, with_labels=True, ax=ax)

    list_hi = list()
    list_of = list()

    for node in graph.nodes():
        if graph.node[node]['club'] == 'Mr. Hi':
            list_hi.append(node)
        if graph.node[node]['club'] == 'Officer':
            list_of.append(node)

    nx.draw_networkx_nodes(graph, pos=pos, nodelist=list_of, node_color='b', ax=ax)
    nx.draw_networkx_nodes(graph, pos=pos, nodelist=list_hi, node_color='g', ax=ax)

    return ax


def create_digraph(ids2ids, start_node='348785149'):
    '''
    Creates a graph of friends of friends for the initial user 'start_node'.

    Paramters
    ---------
    ids2ids: A dictionary.

    Returns
    -------
    A networkx.DiGraph instance.
    '''

    dg = nx.DiGraph()
    dg.add_node(start_node)

    for id in ids2ids:
        for fof in ids2ids[id]:
            if fof in ids2ids:
                dg.add_edge(id, fof)

    return dg


def draw_social_graph(graph):
    '''
    Draws the "graph".

    Paramters
    ---------
    graph: A networkx.DiGraph instance.

    Returns
    -------
    A matplotlib.Axes instance.
    '''

    fig, ax = plt.subplots(figsize=(20, 20))

    ax.grid(b=False)
    ax.set_axis_bgcolor('white')
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])


    pos = nx.spring_layout(graph)

    nx.draw_networkx_nodes(graph, pos, ax=ax, node_color=sns.xkcd_rgb["denim blue"], alpha=.8)
    nx.draw_networkx_edges(graph, pos, ax=ax, edge_color=sns.xkcd_rgb["denim blue"], alpha=.4, arrows=False)

    return ax