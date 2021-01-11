import random
import unittest
import time
from typing import List

from src import GraphAlgo as GA
from src import DiGraph as G


class MyTestCase(unittest.TestCase):

    def test_load(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5_edited")
        self.assertEqual(48, g.v_size())
        self.assertEqual(1.4195069847291193, g.get_node(0).getEdgesFrom().get(2))

    def test_save(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5_edited")
        ga.save_to_json("../data/Atest")

        newG: G = G.DiGraph()
        newGA: GA = GA.GraphAlgo(newG)
        newGA.load_from_json("../data/Atest")

        self.assertEqual(g.v_size(), newG.v_size())
        self.assertEqual(g.e_size(), newG.e_size())
        self.assertEqual(g.get_node(0).getLocation(),
        newG.get_node(0).getLocation())  # checks if the same node is in this 2 graphs

    def test_shortestPath1(self):
        g: G = G.DiGraph()
        for i in range(10):
            g.add_node(i)

        g.add_edge(0, 1, 18)
        g.add_edge(0, 4, 1.2)
        g.add_edge(3, 1, 5.4)
        g.add_edge(1, 2, 6.7)
        g.add_edge(4, 3, 2.3)

        ga: GA = GA.GraphAlgo(g)
        self.assertAlmostEqual(15.6, ga.shortest_path(0, 2)[0], delta=0.001)

    def test_shortestPath2(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5")
        tup: tuple = ga.shortest_path(0, 40)

        self.assertEqual(8.502968926650318, tup[0])
        self.assertEqual([0, 2, 3, 13, 14, 15, 39, 40], tup[1])


    def test_allConnected2(self):
        g: G = G.DiGraph()
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 7)
        g.add_edge(3, 4, 6.0)
        g.add_edge(4, 3, 8.0)
        g.add_edge(2, 4, 0.5)
        g.add_edge(4, 2, 7.8)

        ga: GA = GA.GraphAlgo(g)

        self.assertEqual(3, len(ga.connected_components()))

    """creates a graph with 100 nodes"""

    def creatingGraph1(self) -> G:
        g: G = G.DiGraph()
        for i in range(100):
            g.add_node(i)

    """ creates graph with 10^4 nodes"""

    def creatingGraph2(self) -> G:
        g: G = G.DiGraph()
        for i in range(10000):
            g.add_node(i)

    """ creates graph with 10^6 nodes"""

    def creatingGraph3(self) -> G:
        g: G = G.DiGraph()
        for i in range(1000000):
            g.add_node(i)

    def test_creating1(self):
        start = float(time.time())
        self.creatingGraph1()
        end = float(time.time())

    def test_creating2(self):
        start = float(time.time())
        self.creatingGraph2()
        end = float(time.time())

    def test_creating3(self):
        start = float(time.time())
        self.creatingGraph3()
        end = float(time.time())

    def test_shortestPathTime(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A3")

        start = float(time.time())
        ans: tuple = ga.shortest_path(0, 41)
        end = float(time.time())
        print("shortest path on A3 graph Time in seconds: " + str(end - start))
        print("From source:0 to dest: 41", ans)
        print("")

    def test_loadTime(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)

        start = float(time.time())
        ga.load_from_json("../data/A3")
        end = float(time.time())

        self.assertEqual(49, g.v_size())
        self.assertEqual(136, g.e_size())
        print("loading A3 graph, |V| = 49, |E| = 136")
        print("time it takes in seconds: ", str(end - start))
        print("")


    def test_save(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5")

        start = float(time.time())
        ga.save_to_json("../data/Atest")
        end = float(time.time())
        print("Testing sace function on A5 graph")
        print("Time it takes in seconds: " + str(end - start))
        print("")


    def test_connected(self):  # small graph
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5_edited")

        start = float(time.time())
        ans: List[list] = ga.connected_components()
        end = float(time.time())
        print("Testing connected_components on A5_edited")
        print("first component: ", ans[0])
        print("second component: ", ans[1])
        print("Time in it takes seconds: " + str(end - start))
        print("")

    def test_connectedBig(self):  # 30K and 240K
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/G_30000_240000_0.json")

        #  {"src": 0, "w": 69.21467975989786, "dest": 28846}
        self.assertEqual(69.21467975989786, g.get_node(0).getEdgesFrom().get(28846))

        start = float(time.time())
        ans: List[list] = ga.connected_components()
        end = float(time.time())
        timeItTakes: float = end - start

        print("Testing connected_components on: ", str(g.v_size()), " NODES, and: ", str(g.e_size()), " EDGES")
        print("It takes: ", str(timeItTakes), " seconds")
        print("")


    def test_shortestPath(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/G_30000_240000_0.json")

        start = float(time.time())
        path: tuple = ga.shortest_path(0, 53)
        end = float(time.time())
        timeItTakes: float = end - start
        print("Shortest path on graph with |V| = 30k, |E|= 240k")
        print("Shortest path from 0 to 53 by weight of edges is: ", path[0])
        print("The path is: ", path[1])
        print("Testing connected_components on: ", str(g.v_size()), " NODES, and: ", str(g.e_size()), " EDGES")
        print("It takes: ", str(timeItTakes), " seconds")
        print("")

    def test_connected_component(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/G_30000_240000_0.json")

        print("Test connected_component on graph with |V|=30, |E|=240k ")
        start = float(time.time())
        ans: list = ga.connected_component(2)
        end = float(time.time())
        timeItTakes: float = end - start
        print("It takes: ", str(timeItTakes), " seconds")

        print("")

    def test_connected_components(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/G_30000_240000_0.json")

        print("Test connected_component on graph with |V|=30, |E|=240k ")
        start = float(time.time())
        ans: List[list] = ga.connected_components()
        end = float(time.time())
        timeItTakes: float = end - start
        print("It takes: ", str(timeItTakes), " seconds")
        print(len(ans))
        print("")


    def test_plot(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A3")
        ga.plot_graph()

if __name__ == '__main__':
    unittest.main()
