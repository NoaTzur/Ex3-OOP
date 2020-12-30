import random

from src.GraphInterface import GraphInterface
import src.node_data as Node


class DiGraph(GraphInterface):

    def __init__(self):  # (key-id, node_data)
        self.myGraph = dict()
        self.MC = 0
        self.edgesCounter = 0

    def __repr__(self):
        return "Graph: |V|=" + str(len(self.myGraph)) + " |E|=" + str(self.edgesCounter)

    def get_node(self, key: int) -> Node:
        return self.myGraph.get(key)

    def v_size(self) -> int:
        return len(self.myGraph.keys())

    def e_size(self) -> int:
        return self.edgesCounter

    def get_all_v(self) -> dict:
        return self.myGraph

    def all_in_edges_of_node(self, id1: int) -> dict:
        node: Node = self.myGraph.get(id1)
        if node is None:
            return None

        return node.getEdgesTo()

    def all_out_edges_of_node(self, id1: int) -> dict:
        node = self.myGraph.get(id1, Node)  # returns NodeClass with id1
        return node.getEdgesFrom()

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        node1: Node = self.myGraph.get(id1, Node)
        node2: Node = self.myGraph.get(id2, Node)

        if(node1 is None) or (node2 is None):
            return False
        if node1.getEdgesFrom().get(id2) is not None:
            return False

        node1.addEdgesFrom(id2, weight)
        node2.addEdgesTo(id1, weight)
        self.MC = self.MC + 1
        self.edgesCounter = self.edgesCounter + 1
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
        node: Node = self.myGraph.get(node_id)
        if node is None:
            return False

        dict1: dict = node.getEdgesTo()
        for key in dict1:
            tempNode: Node = self.myGraph.get(key)
            tempNode.removeEdgesFrom(node_id)
            if node_id in tempNode.getEdgesTo().keys():
                tempNode.removeEdgesTo(node_id)
            self.MC = self.MC + 1
            self.edgesCounter = self.edgesCounter - 1

        node.clearNode()
        del (self.myGraph[node_id])
        self.MC = self.MC + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        node1: Node = self.myGraph.get(node_id1)
        node2: Node = self.myGraph.get(node_id2)

        if (node1 is not None) and (node2 is not None):
            node1.removeEdgesFrom(node_id2)
            node2.removeEdgesTo(node_id1)
            self.MC = self.MC + 1
            self.edgesCounter = self.edgesCounter - 1
            return True
        return False
