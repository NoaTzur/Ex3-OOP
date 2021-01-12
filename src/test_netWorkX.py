import json
import unittest
import time

import networkx as nx


class MyTestCase(unittest.TestCase):

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

        def test_creatingGraph1(self): # 10 nodes and 80 edges
            start = float(time.time())
            G = self.loadJson('../data/G_10_80_0.json')
            end = float(time.time())
            ans = end - start
            print("Creating graph with 10 nodes and 80 edges")
            print("time it takes: ",f'{ans:.10f}')
            print("")

        def test_creatingGraph2(self):
            start = float(time.time())
            G = self.loadJson('../data/G_100_800_0.json')
            end = float(time.time())
            ans = end - start
            print("Creating graph with 100 nodes and 800 edges")
            print("time it takes: ", f'{ans:.10f}')
            print("")


        def test_creatingGraph3(self):
            start = float(time.time())
            G = self.loadJson('../data/G_1000_8000_0.json')
            end = float(time.time())
            ans = end - start
            print("Creating graph with 1000 nodes and 8000 edges")
            print("time it takes: ", f'{ans:.10f}')
            print("")


        def test_creatingGraph4(self):
            start = float(time.time())
            G = self.loadJson('../data/G_10000_80000_0.json')
            end = float(time.time())
            ans = end - start
            print("Creating graph with 10000 nodes and 80000 edges")
            print("time it takes: ", f'{ans:.10f}')
            print("")


        def test_creating5(self):
            G = nx.DiGraph()
            start = float(time.time())
            for i in range(1000000):
                G.add_node(i)
            for j in range(1000000-10):
                G.add_weighted_edges_from([(j, j+1, j+0.5)])

            end = float(time.time())
            ans = end - start
            print("Creating graph with 10^6 nodes and 10^6 edges")
            print("time it takes: ", f'{ans:.10f}')
            print("")


        def test_shortest(self):
            G = self.loadJson('../data/G_30000_240000_0.json')

            start = float(time.time())
            listPath:list = nx.dijkstra_path(G, 0, 53, weight='weight')
            end = float(time.time())

            print("networkX: Testing shortestPath on graph with 30K nodes and 240K edges")
            print("The path is: ", listPath)
            print("Time it takes in seconds: ", f'{end-start:.10f}')
            print("")



        def test_connected_compomemts(self): # all
            G = self.loadJson('../data/G_30000_240000_0.json')
            start = float(time.time())
            allComponents: set = nx.algorithms.strongly_connected_components(G)
            end = float(time.time())
            print("checks the load process: |E|= ", G.number_of_edges(), "|V|= ", G.number_of_nodes())
            print("networkX: Testing connected_components on graph with 30K nodes and 240K edges")
            print("Time it takes in seconds: ", f'{end-start:.10f}')
            print("")


        def test_connected_compomemt(self): # specific node is in the list
            G = self.loadJson('../data/A5_edited')

            start = float(time.time())
            allComponents: set = nx.algorithms.strongly_connected_components(G)
            for i in allComponents:
                if 0 in i:
                    print("Component that contains node with key 0:", i)
            end = float(time.time())
            ans = end - start
            print("")

if __name__ == '__main__':
    unittest.main()
