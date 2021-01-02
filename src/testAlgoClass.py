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

    def test_allConnected1(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5")
        random.seed(55555)
        for i in range(1000):
            b = random.randint(0, 47)
            c = random.randint(0, 47)
            g.remove_edge(b, c)
            g.remove_edge(c, b)
        for i in g.get_all_v().keys():
            print(ga.connected_component(i))

    def test_allConnected2(self):
        g: G = G.DiGraph()
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 7)
        # g.add_edge(1,0,6)

        g.add_edge(3, 4, 6.0)
        g.add_edge(4, 3, 8.0)
        g.add_edge(2, 4, 0.5)
        g.add_edge(4, 2, 7.8)

        ga: GA = GA.GraphAlgo(g)

        print(ga.connected_components())

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
        print("100 nodes - Time in seconds: " + str(end-start))

    def test_creating2(self):
        start = float(time.time())
        self.creatingGraph2()
        end = float(time.time())
        print("10^4 nodes - Time in seconds: " + str(end - start))

    def test_creating3(self):
        start = float(time.time())
        self.creatingGraph3()
        end = float(time.time())
        print("10^6 nodes - Time in seconds: " + str(end - start))

    def test_shortestPathTime(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A3")

        start = float(time.time())
        ans: tuple = ga.shortest_path(0, 41)
        end = float(time.time())
        print("Time in seconds: " + str(end-start))
        print(ans)

    def test_loadTime(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)

        start = float(time.time())
        ga.load_from_json("../data/A3")
        end = float(time.time())
        print("Time in seconds: " + str(end - start))

        self.assertEqual(49, g.v_size())
        self.assertEqual(136, g.e_size())
        print("after loading, |V| = 49, |E| = 136")

    def test_save(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5")

        start = float(time.time())
        ga.save_to_json("../data/Atest")
        end = float(time.time())
        print("Time in seconds: " + str(end - start))

    def test_connected(self):
        g: G = G.DiGraph()
        ga: GA = GA.GraphAlgo(g)
        ga.load_from_json("../data/A5_edited")

        start = float(time.time())
        ans: List[list] = ga.connected_components()
        end = float(time.time())
        print("Time in seconds: " + str(end - start))
        print(ans[0])
        print(ans[1])

if __name__ == '__main__':
    unittest.main()
