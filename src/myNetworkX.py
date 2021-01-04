import json
import unittest
import time

import networkx as nx


class MyTestCase(unittest.TestCase):


        def creatingGraph1(self):
            G = nx.DiGraph()
            for i in range(100):
                G.add_node(i)

        """ creates graph with 10^4 nodes"""

        def creatingGraph2(self):
            G = nx.DiGraph()
            for i in range(10000):
                G.add_node(i)

        """ creates graph with 10^6 nodes"""

        def creatingGraph3(self):
            G = nx.DiGraph()
            for i in range(1000000):
                G.add_node(i)

        def test_creating1(self):
            start = float(time.time())
            self.creatingGraph1()
            end = float(time.time())
            ans = end-start
            print(f'{ans:.10f}')

        def test_creating2(self):
            start = float(time.time())
            self.creatingGraph2()
            end = float(time.time())
            ans = end - start
            print(f'{ans:.10f}')

        def test_creating3(self):
            start = float(time.time())
            self.creatingGraph3()
            end = float(time.time())
            ans = end - start
            print(f'{ans:.10f}')

        def loadJson(self, filename) -> nx :
            G = nx.DiGraph()
            with open(filename, 'r') as file:
                json_graph = json.load(file)

            nodes: list = json_graph['Nodes']
            edges: list = json_graph['Edges']
            number_of_nodes: int = len(nodes)
            number_of_edges: int = len(edges)

            for i in range(number_of_nodes):
                nodeToConvert: dict = nodes[i]  # looks like: {'id': 0, 'pos': '35.212217299435025,32.106235628571426,0.0'}
                key: int = nodeToConvert.get('id')
                G.add_node(key)

          #  list_of_tup_edges: list = []
            # list_of_tup_edges looks like - [(1,3,6.7), (4,6,0,45).....]
            # for example - 1 is the src, 3 is the destination node and 6.7 is the weight
            for j in range(number_of_edges):
                edgeToConvert: dict = edges[j]  # looks like: {'src': 0, 'dest': 1, 'w': 1.0286816758196655}
                srcNode: int = edgeToConvert.get('src')
                destNode: int = edgeToConvert.get('dest')
                weight: float = edgeToConvert.get('w')
                G.add_weighted_edges_from([(srcNode, destNode, weight)])

           # G.add_weighted_edges_from(list_of_tup_edges) # add_weighted_edges_from adds list of edges at once

            return G

        def test_shortest(self):
            G = self.loadJson('../data/A3')

            start = float(time.time())
            print(nx.shortest_path(G, source=0, target=41))
            end = float(time.time())
            ans = end-start
            print(f'{ans:.10f}')


        def test_connected_compomemts(self): # all
            G = self.loadJson('../data/A5_edited')
            start = float(time.time())
            allComponents: set = nx.algorithms.strongly_connected_components(G)
            end = float(time.time())
            ans = end - start
            print(f'{ans:.10f}')

        def test_connected_compomemt(self): # specific node is in the list
            G = self.loadJson('../data/A5_edited')

            start = float(time.time())
            allComponents: set = nx.algorithms.strongly_connected_components(G)
            for i in allComponents:
                if 0 in i:
                    print(i)
            end = float(time.time())
            ans = end - start
            print(f'{ans:.10f}')


if __name__ == '__main__':
    unittest.main()
