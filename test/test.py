import pytest
import networkx as nx
import src.graph as g
# Import fungsi yang telah dibuat
def test_graph_creation():
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]
    G = g.create_graph(edges)
    assert len(G.nodes) == 5
    assert len(G.edges) == 6

def test_degree():
    G = g.create_graph([(1, 2), (2, 3), (3, 4)])
    assert g.get_degree(G, 2) == 2

def test_dfs_traversal():
    G = g.create_graph([(1, 2), (2, 3), (3, 4)])
    assert g.dfs_traversal(G, 1) == [1, 2, 3, 4]

def test_bfs_traversal():
    G = g.create_graph([(1, 2), (1, 3), (3, 4)])
    assert g.bfs_traversal(G, 1) == [1, 2, 3, 4]

def test_shortest_path():
    G = g.create_graph([(1, 2), (2, 3), (3, 4)])
    assert g.find_shortest_path(G, 1, 4) == [1, 2, 3, 4]

if __name__ == "__main__":
    pytest.main()