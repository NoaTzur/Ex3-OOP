import random

from src.GraphInterface import GraphInterface
import src.node_data as Node


class DiGraph(GraphInterface):

    def __init__(self):  # (key-id, NodeClass)
        self.myGraph = dict()
        self.MC = 0
        self.edgesCounter = 0

    def __repr__(self):
        return "Graph: |V|=" + str(len(self.myGraph)) + " |E|=" + str(self.edgesCounter)

    def v_size(self) -> int:
        return len(self.myGraph.keys())

    def e_size(self) -> int:
        return self.edgesCounter

    def get_all_v(self) -> dict:
        return self.myGraph

    def all_in_edges_of_node(self, id1: int) -> dict:
        node = self.myGraph.get(id1, Node)  # returns NodeClass with id1
        return node.getEdgesTo()

    def all_out_edges_of_node(self, id1: int) -> dict:
        node = self.myGraph.get(id1, Node)  # returns NodeClass with id1
        return node.getEdgesFrom()

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        node1: Node = self.myGraph.get(id1, Node)
        node2: Node = self.myGraph.get(id2, Node)

        if (node1 is not None) and (node2 is not None):

            dict1 = node1.getEdgesFrom()
            if dict1.get(id2) == weight:
                return False

            if dict1.get(id2) is None:
                self.edgesCounter = self.edgesCounter + 1

            node1.addEdgesFrom(id2, weight)
            node2.addEdgesTo(id1, weight)
            self.MC = self.MC + 1

        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.myGraph.get(node_id) is not None:
            return False

        if pos is None:
            x = random.randint(1, 20)
            y = random.randint(1, 20)
            pos = (x, y)

        newNode: Node = Node.node_data(node_id, pos)
        self.myGraph[node_id] = newNode
        self.MC = self.MC + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        node = self.myGraph.get(node_id, Node)
        if node is None:
            return False

        dict1: dict = node.getEdgesTo()
        for key in dict1:
            tempNode = self.myGraph.get(key, Node)
            tempNode.removeEdgesFrom(node_id)
            self.MC = self.MC + 1
            self.edgesCounter = self.edgesCounter - 1

        node.clearNode()
        del (self.myGraph[node_id])
        self.MC = self.MC + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        node1 = self.myGraph.get(node_id1, Node)
        node2 = self.myGraph.get(node_id2, Node)

        if (node1 is not None) and (node2 is not None):
            node1.removeEdgesFrom(node_id2)
            node2.removeEdgesTo(node_id1)
            self.MC = self.MC + 1
            self.edgesCounter = self.edgesCounter - 1
            return True
        return False
