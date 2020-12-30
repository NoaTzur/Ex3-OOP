import json
import heapq as hq

from typing import List

from src import DiGraph as Graph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
import src.node_data as Node



class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.currGraph: Graph = Graph.DiGraph()
        self.parents: dict = dict()
        self.visitedNodes: dict = dict()  # 0-White, 1-Gray, 2-Black
        self.counter: int = 0

    def get_graph(self) -> GraphInterface:
        return self.currGraph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            json_graph = json.load(file)

        nodes: list = json_graph['Nodes']
        edges: list = json_graph['Edges']
        number_of_nodes: int = len(nodes)
        number_of_edges: int = len(edges)

        for i in range(number_of_nodes):
            nodeToConvert: dict = nodes[i]  # looks like: {'id': 0, 'pos': '35.212217299435025,32.106235628571426,0.0'}
            key: int = nodeToConvert.get('id')
            pos: str = nodeToConvert.get('pos')
            x: float = float(pos.split(",")[0])  # convert x position to float from string
            y: float = float(pos.split(",")[1])  # convert y position to float from string
            self.currGraph.add_node(key, (x, y))

        for j in range(number_of_edges):
            edgeToConvert: dict = edges[j]  # looks like: {'src': 0, 'dest': 1, 'w': 1.0286816758196655}
            srcNode: int = edgeToConvert.get('src')
            destNode: int = edgeToConvert.get('dest')
            weight: float = edgeToConvert.get('w')
            self.currGraph.add_edge(srcNode, destNode, weight)

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, 'w') as file:
            json.dump(self.currGraph, file)
            return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.parents.clear()
        shortestPathNum: float = self.Dijkstra_float(id1, id2)
        if shortestPathNum is not -1:
            shortestPathList: list = self.Dijkstra_path(id1, id2)
        else:
            return -1, None

        return shortestPathNum, shortestPathList

    def Dijkstra_float(self, src: int, dest: int) -> float:
        if src is dest:
            return 0
        hasVisited = dict()  # <key-id: int, 0\1: int>
        node: Node.node_data = self.currGraph.get_node(src)
        node.setTag(0)

        listOfNodes = []
        listOfNodes.append((node.getTag(), node))
        hq.heapify(listOfNodes)

        while len(listOfNodes) is not 0:
            tempNode: Node = hq.heappop(listOfNodes)[1]
            if hasVisited.get(tempNode.getKey()) is None:
                for node_neigh, w in tempNode.getEdgesFrom():
                    dist: float = tempNode.getTag() + w
                    n1: Node = self.currGraph.get_node(node_neigh)
                    if dist < n1.getTag():
                        n1.setTag(dist)
                        hq.heappush(listOfNodes, (dist, n1))
                        self.parents[node_neigh] = tempNode.getKey()

                if tempNode.getKey() is dest:
                    return tempNode.getTag()
                hasVisited[tempNode.getKey()] = 1

        return -1

    def Dijkstra_path(self, src: int, dest: int) -> list:
        path: list = []
        if src is dest:
            path.append(self.currGraph.get_node(src))
            return path

        path.append(self.currGraph.get_node(dest))
        parentNode: Node = self.currGraph.get_node(self.parents.get(dest))

        while parentNode is not None:
            if parentNode not in path:  # checks if the contains function know to check if node is contains
                path.insert(0, parentNode)

            if self.parents.get(parentNode.getKey()):  # checks get_node !!!!! does not return Node ????
                parentNode = self.currGraph.get_node(self.parents.get(parentNode.getKey()))
                if parentNode.getKey() is src:
                    path.insert(0, self.currGraph.get_node(src))
                    parentNode = None
            else:
                parentNode = None

        return path

    def connected_component(self, id1: int) -> list:

        if id1 not in self.currGraph.get_all_v().keys():
            return []

        allComponents: List[list] = self.connected_components()
        for i in range(self.counter):
            if id1 in allComponents[i]:
                return allComponents[i]

    def connected_components(self) -> List[list]:
        self.counter = 0
        allComponents = []
        self.visitedNodes.clear()
        """ creates number of list (as number od counter-number of the components in the graph)
        and append the lists to the Main List """
        for i in range(self.counter):
            allComponents.insert(i, [])

        for nodes in self.currGraph.get_all_v().values():
            allComponents[nodes.getComponentMark()].append(nodes.getKey())

        return allComponents

    def DFS(self):
        for nodeKey in self.currGraph.get_all_v().keys():
            self.visitedNodes[nodeKey] = 0

        for node in self.currGraph.get_all_v().keys():
            self.DFSvisit(node)
            self.counter = self.counter+1

    def DFSvisit(self, src: int):
        self.visitedNodes[src] = 1
        self.currGraph.get_node(src).setComponentMark(self.counter)
        for node_neigh in self.currGraph.get_node(src).getEdgesFrom().keys():
            path: float = self.shortest_path(node_neigh, src)[0]

            if self.visitedNodes.get(node_neigh) is 0 and path > 0:
                self.currGraph.get_node(node_neigh).setComponentMark(self.counter)
                self.DFSvisit(node_neigh)

            self.visitedNodes[src] = 2  # needs to be outside the for ?



    def plot_graph(self) -> None:
        pass

