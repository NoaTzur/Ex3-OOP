from src import GraphInterface, NodeClass



class DiGraph(GraphInterface):

    def __init__(self):  # (key-id, NodeClass)
        self.myGraph = dict()
        self.MC = 0
        self.edgesCounter = 0

    def v_size(self) -> int:
        return len(self.myGraph.keys())

    def e_size(self) -> int:
        return self.edgesCounter

    def get_all_v(self) -> dict:
        return self.myGraph

    def all_in_edges_of_node(self, id1: int) -> dict:
        node = self.myGraph[id1]  # returns NodeClass with id1
        return node.NodeClass.gettoList()

    def all_out_edges_of_node(self, id1: int) -> dict:
        node = self.myGraph[id1]  # returns NodeClass with id1
        return node.NodeClass.getfromList()

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        node1 = self.myGraph.get(id1, NodeClass)
        node2 = self.myGraph.get(id2, NodeClass)

        if (node1 is not None) and (node2 is not None):

            dict1 = node1.NodeClass.getEdgesFrom()
            if dict1.get(id2) == weight:
                return False

            if dict1.get(id2) is None:
                self.edgesCounter = self.edgesCounter + 1

            node1.NodeClass.addEdgesFrom(id2, weight)
            node2.NodeClass.addEdgesTo(id1, weight)
            self.MC = self.MC + 1

        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.myGraph.get(node_id) is not None:
            return False

        newNode = NodeClass(node_id, pos)
        self.myGraph[node_id] = newNode
        self.MC = self.MC + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        node = self.myGraph.get(node_id, NodeClass)
        if node is None:
            return False

        dict1 = node.NodeClass.getEdgesTo()
        for key in dict1:
            tempNode = self.myGraph.get(key, NodeClass)
            tempNode.NodeClass.removeEdgesFrom(node_id)
            self.MC = self.MC+1
            self.edgesCounter = self.edgesCounter-1

        node.NodeClass.clearNode()
        del(self.myGraph[node_id])
        self.MC = self.MC + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        node1 = self.myGraph.get(node_id1, NodeClass)
        node2 = self.myGraph.get(node_id2, NodeClass)

        if(node1 is not None) and (node2 is not None):
            node1.NodeClass.removeEdgesFrom(node_id2)
            node2.NodeClass.removeEdgesTo(node_id1)
            self.MC = self.MC+1
            self.edgesCounter = self.edgesCounter-1
            return True
        return False
