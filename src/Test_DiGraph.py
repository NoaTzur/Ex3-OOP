import time
import unittest

from src.DiGraph import DiGraph as G
from src import GraphAlgo as GA

class MyTestCase(unittest.TestCase):

    def test_e_v(self):
        g = G()
        print("empty")
        self.assertEqual(0, g.get_mc(), "MC check")
        print(g)
        for n in range(6):
            g.add_node(n)

        g.add_edge(0, 1, 2)
        g.add_edge(0, 3, 2)
        g.add_edge(2, 0, 4)
        g.add_edge(0, 4, 3)
        g.add_edge(2, 5, 5)
        g.add_edge(5, 2, 1)
        g.add_edge(4, 5, 6)

        self.assertEqual(13, g.get_mc(), "MC check after adding nodes and edges")
        print("mc: ", g.get_mc())

        self.assertEqual(6, g.v_size(), "v_size check")
        self.assertEqual(7, g.e_size(), "e_size check")
        print(g)

        g.remove_node(0)
        """after deleting 0, mc needs to raise in 5 - 1 for the node deletion, 3 for the 3 edges from 0 to others 
        and 1 for the edge from 2 to 0"""
        self.assertEqual(18, g.get_mc(), "MC check after removing node with edges")
        self.assertEqual(3, g.e_size())
        self.assertEqual(5, g.v_size())

        g.add_node(7)

        self.assertEqual(19, g.get_mc())
        g.add_edge(5, 7, 5)
        g.add_edge(4, 7, 3)

        self.assertEqual(5, g.e_size())
        self.assertEqual(6, g.v_size())
        print("")

    def test_pos(self):
        g = G()
        pos1 = (1, 2)
        pos2 = (3, 4)
        pos3 = (5, 6)
        pos4 = (7, 8)
        g.add_node(1, pos1)
        g.add_node(2, pos2)
        g.add_node(3, pos3)
        g.add_node(4, pos4)
        print(g)
        print("the current graph ->")
        print(g.get_all_v())
        print("mc: ", g.get_mc())
        print("")

    def test_remove_edges(self):
        g = G()
        for i in range(1000):
            g.add_node(i)

        for edge in range(990):
            g.add_edge(edge, edge+2,edge+0.8)

        self.assertEqual(990, g.e_size())
        print("removing 7 edges, after this action - the number of edges should be 983")
        g.remove_edge(0, 2)
        g.remove_edge(1, 3)
        g.remove_edge(2, 4)
        g.remove_edge(3, 5)
        g.remove_edge(4, 6)
        g.remove_edge(5, 7)
        g.remove_edge(6, 8)
        self.assertEqual(983, g.e_size())
        print("Number of edges is:", g.e_size())
        g.remove_edge(0,2)
        self.assertEqual(983, g.e_size()) # removing edge that does not exist- do nothing
        print("")

    def test_create_1(self):  # 10 nodes and 80 edges
        g: G = G()
        ga: GA = GA.GraphAlgo(g)
        start = float(time.time())
        ga.load_from_json("../data/G_10_80_0.json")
        end = float(time.time())

        #  {"src":5,"w":10.383183147587454,"dest":3}
        self.assertEqual(10.383183147587454, g.get_node(5).getEdgesFrom().get(3))

        print("Creating graph with 10 nodes and 80 edges: ", str(g.v_size()), " NODES, and: ", str(g.e_size()), " EDGES")
        print("It takes: ", f'{end-start:.10f}', " seconds")
        print("")

    def test_create_2(self):  # 100 nodes and 800 edges
        g: G = G()
        ga: GA = GA.GraphAlgo(g)
        start = float(time.time())
        ga.load_from_json("../data/G_100_800_0.json")
        end = float(time.time())

        #  {"src":64,"w":26.4615978682933,"dest":8}
        self.assertEqual(26.4615978682933, g.get_node(64).getEdgesFrom().get(8))

        print("Creating graph with 100 nodes and 800 edges: ", str(g.v_size()), " NODES, and: ", str(g.e_size()),
              " EDGES")
        print("It takes: ", f'{end - start:.10f}', " seconds")
        print("")

    def test_create_3(self):  # 1000 nodes and 8000 edges
        g: G = G()
        ga: GA = GA.GraphAlgo(g)
        start = float(time.time())
        ga.load_from_json("../data/G_1000_8000_0.json")
        end = float(time.time())

        #  {"src":2,"w":70.95459152756798,"dest":133},
        self.assertEqual(70.95459152756798, g.get_node(2).getEdgesFrom().get(133))

        print("Creating graph with 1000 nodes and 8000 edges: ", str(g.v_size()), " NODES, and: ", str(g.e_size()),
              " EDGES")
        print("It takes: ", f'{end - start:.10f}', " seconds")
        print("")


    def test_create_4(self):  # 10000 nodes and 80000 edges
        g: G = G()
        ga: GA = GA.GraphAlgo(g)
        start = float(time.time())
        ga.load_from_json("../data/G_10000_80000_0.json")
        end = float(time.time())

        #  {"src":9,"w":79.59769700285791,"dest":3448}
        self.assertEqual(79.59769700285791, g.get_node(9).getEdgesFrom().get(3448))

        print("Creating graph with 10000 nodes and 80000 edges: ", str(g.v_size()), " NODES, and: ", str(g.e_size()),
              " EDGES")
        print("It takes: ", f'{end - start:.10f}', " seconds")
        print("")

    def test_create_5(self):
        g: G = G()
        start = float(time.time())

        for i in range(1000000):
            g.add_node(i)
        for j in range(1000000 - 10):
            g.add_edge(j, j+1, j+0.6)

        end = float(time.time())
        print("It takes: ", f'{end - start:.10f}', " seconds")

if __name__ == '__main__':
    unittest.main()
