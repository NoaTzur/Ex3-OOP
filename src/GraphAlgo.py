import json
import heapq as hq
import random
import matplotlib.pyplot as plt
from typing import List

from src import DiGraph as Graph, DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
import src.node_data as Node


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: Graph = Graph.DiGraph()):
        self.currGraph: Graph = g
        self.parents: dict = dict()
        self.visitedNodes: dict = dict()  # 0-White, 1-Gray, 2-Black
        self.counter: int = 0

    def get_graph(self) -> DiGraph:
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
            if pos is None:
                x = random.randint(1, 20)
                y = random.randint(1, 20)
                self.currGraph.add_node(key, (x, y))
            else:
                x: float = float(pos.split(",")[0])  # convert x position to float from string
                y: float = float(pos.split(",")[1])  # convert y position to float from string
                self.currGraph.add_node(key, (x, y))

        for j in range(number_of_edges):
            edgeToConvert: dict = edges[j]  # looks like: {'src': 0, 'dest': 1, 'w': 1.0286816758196655}
            srcNode: int = edgeToConvert.get('src')
            destNode: int = edgeToConvert.get('dest')
            weight: float = edgeToConvert.get('w')
            self.currGraph.add_edge(srcNode, destNode, weight)
        return True

    def save_to_json(self, file_name: str) -> bool:
        listOfNodes: list = []
        i: int = 0
        for node in self.currGraph.get_all_v().values():
            pos: tuple = node.getLocation()
            st = str(pos[0]) + "," + str(pos[1])
            listOfNodes.insert(i, {"id": node.getKey(), "pos": st})
            i+=1

        listOfEdges: list = []
        j: int = 0
        for node_key in self.currGraph.get_all_v().keys():
            for node_neigh in self.currGraph.all_out_edges_of_node(node_key).keys():
                weight: float = self.currGraph.all_out_edges_of_node(node_key).get(node_neigh)
                listOfEdges.insert(j, {"src": node_key, "dest": node_neigh, "w": weight})
                j+=1

        graph_dict: dict = {"Nodes": listOfNodes, "Edges": listOfEdges}

        with open(file_name, 'w') as file:
            json.dump(graph_dict, file)
            return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.parents.clear()
        for node in self.currGraph.get_all_v().values():
            node.setTag(float('inf'))

        shortestPathNum: float = self.Dijkstra_float(id1, id2)
        if shortestPathNum != float('inf'):
            shortestPathList: list = self.Dijkstra_path(id1, id2)
        else:
            return float('inf'), []

        return shortestPathNum, shortestPathList

    def Dijkstra_float(self, src: int, dest: int) -> float:
        if src == dest:
            return 0
        hasVisited = dict()  # <key-id: int, 0\1: int>
        node: Node.node_data = self.currGraph.get_node(src)
        node.setTag(0)

        listOfNodes = []
        listOfNodes.append((node.getTag(), node))
        hq.heapify(listOfNodes)

        while len(listOfNodes) != 0:
            tempNode: Node = hq.heappop(listOfNodes)[1]
            if hasVisited.get(tempNode.getKey()) is None:
                for node_neigh, w in tempNode.getEdgesFrom().items():
                    dist: float = tempNode.getTag() + w
                    n1: Node = self.currGraph.get_node(node_neigh)
                    if dist < n1.getTag():
                        n1.setTag(dist)
                        hq.heappush(listOfNodes, (dist, n1))
                        self.parents[node_neigh] = tempNode.getKey()

                if tempNode.getKey() == dest:
                    return tempNode.getTag()
                hasVisited[tempNode.getKey()] = 1

        return float('inf')

    def Dijkstra_path(self, src: int, dest: int) -> list:
        path: list = []
        if src == dest:
            path.append(src)
            return path

        path.append(dest)
        parentNode: int = self.parents.get(dest)

        while parentNode != -1:
            if parentNode not in path:  # checks if the contains function know to check if node is contains
                path.insert(0, parentNode)

            if self.parents.get(parentNode) is not None:
                parentNode = self.parents.get(parentNode)
                if parentNode == src:
                    path.insert(0, parentNode)
                    parentNode = -1
            else:
                parentNode = -1

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
        self.DFS()
        """ creates number of list (as number od counter-number of the components in the graph)
        and append the lists to the Main List """
        for i in range(self.counter):
            allComponents.insert(i, [])

        for nodes in self.currGraph.get_all_v().values():
            allComponents[nodes.getComponentMark()].append(nodes.getKey())

        filteredList: list = []

        for i in range(len(allComponents)):
            if len(allComponents[i]) > 0:
                filteredList.append(allComponents[i])

        return filteredList

    def DFS(self):
        for nodeKey in self.currGraph.get_all_v().keys():
            self.visitedNodes[nodeKey] = 0

        for node in self.currGraph.get_all_v().keys():
            self.DFSvisit(node)
            self.counter = self.counter+1

    def DFSvisit(self, src: int):
        if self.visitedNodes.get(src) == 0:
            self.currGraph.get_node(src).setComponentMark(self.counter)

        self.visitedNodes[src] = 1
        for node_neigh in self.currGraph.get_node(src).getEdgesFrom().keys():
            path: float = self.shortest_path(node_neigh, src)[0]

            if self.visitedNodes.get(node_neigh) == 0 and path != float('inf'):
                self.currGraph.get_node(node_neigh).setComponentMark(self.counter)
                self.DFSvisit(node_neigh)

        self.visitedNodes[src] = 2  # needs to be outside the for ?

    def plot_graph(self):
        ax=plt.axes()
        ax.set_facecolor('lightpink')
        R=0.00045
        for node in self.currGraph.get_all_v():
            x=self.currGraph.get_node(node).getLocation()[0]
            y=self.currGraph.get_node(node).getLocation()[1]
            ax.plot(x,y, marker='o', markersize=5,
                    markerfacecolor="black", markeredgewidth=1, markeredgecolor="black")
            for newnode in self.currGraph.get_node(node).getEdgesFrom():
                x1=self.currGraph.get_node(newnode).getLocation()[0]
                y1=self.currGraph.get_node(newnode).getLocation()[1]
                dirx=(x-x1)/math.sqrt(math.pow(x-x1,2)+math.pow((y-y1),2))-R
                diry=(y-y1)/math.sqrt(math.pow(x-x1,2)+math.pow((y-y1),2))-R
                p1x=dirx*R+x1
                p1y=diry*R+y1
                plt.arrow(x,y,p1x-x,p1y-y,head_width=R*0.6,head_length=R-0.0001,width=R*R, ec="purple", fc="purple")
        plt.title('GRAPH',fontsize = 18, fontweight ='bold')
        plt.show()

