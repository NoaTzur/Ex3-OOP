import random
import unittest

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
        print(ga.shortest_path(3, 4)[0])
        print(ga.connected_components())


if __name__ == '__main__':
    unittest.main()
