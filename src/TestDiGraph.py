import unittest

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_e_v(self):
        g = DiGraph()
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

    def test_pos(self):
        g = DiGraph()
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


    def test_remove_edges(self):
        g = DiGraph()
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

        g.remove_edge(0,2)
        self.assertEqual(983, g.e_size()) # removing edge that does not exist- do nothing



if __name__ == '__main__':
    unittest.main()
