import unittest
from pypolish import jaccard_index, graph_polishing


class TestSimilarity(unittest.TestCase):
    def test_graph_polishing_dict1(self):
        graph = {'A': ['B', 'C'],
                 'B': ['A', 'C'],
                 'C': ['A', 'B']}
        res = graph_polishing(graph, 1.0/3.0, 10, jaccard_index)
        self.assertEqual(graph.keys(), res.keys())
        for k in graph.keys():
            graph[k].sort()
            res[k].sort()
            self.assertEqual(graph[k], res[k])
